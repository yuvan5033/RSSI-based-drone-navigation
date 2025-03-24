import threading
import time
import yaml
from bleak import BleakScanner, BleakError
from ..drone_control.kalman_filter import KalmanFilter
import asyncio
import aioblescan as aiobs

def decode(data):
    ev = aiobs.HCI_Event()
    ev.decode(data)
    print(ev)
# Constants
CONFIG_FILE = "config.yaml"
SCAN_INTERVAL = 2  # Scan every 2 seconds

def load_config():
    """Load beacon UUIDs and locations from the config file."""
    try:
        with open(CONFIG_FILE, "r") as file:
            config = yaml.safe_load(file)
        return config.get("beacons", {})
    except Exception as e:
        print(f"[ERROR] Failed to load config: {e}")
        return {}

# Load beacon config
BEACONS = load_config()

# Initialize Kalman filters for all UUIDs in the config
filters = {uuid: KalmanFilter() for uuid in BEACONS.keys()}

TARGET_MAC = "74:4D:BD:61:E1:61"  # Example: "84:CC:A8:00:1A:29"
async def main():
    event_loop = asyncio.get_event_loop()
    mysocket = aiobs.create_bt_socket(0)
    fac = event_loop.create_connection(lambda: aiobs.BLEScanRequester(decode), mysocket)
    await fac
async def scan_by_mac():
    """Scan for BLE devices and extract UUID of the target MAC."""
    print(f"[BLE] Scanning for {TARGET_MAC}...")

    devices = await BleakScanner.discover(timeout=10)

    found = False
    for device in devices:
        if device.address.lower() == TARGET_MAC.lower():
            found = True
            print(f"[FOUND] {device.name or 'Unknown'} [{device.address}] - RSSI: {device.rssi}")

            # Extract and display UUIDs if available
            if device.metadata and "uuids" in device.metadata:
                uuids = device.metadata["uuids"]
                print(f"→ UUIDs: {', '.join(uuids) if uuids else 'None'}")
            else:
                print("[INFO] No UUIDs found in metadata.")
            
            break
    
    if not found:
        print(f"[ERROR] Device with MAC {TARGET_MAC} not found.")


async def scan_ble():
    """Asynchronously scans and displays all BLE devices."""
    print("[BLE] Scanning for devices...")

    try:
        devices = await BleakScanner.discover(return_adv=True)
        detected = {}

        for device, adv in devices.values():
            # Extract UUIDs from advertisement data
            uuids = adv.service_uuids
            rssi = device.rssi

            # Apply Kalman filtering if UUID is in config, otherwise display raw RSSI
            for uuid in uuids:
                if uuid in BEACONS:
                    filtered_rssi, error = filters[uuid].update(rssi)
                else:
                    filtered_rssi, error = rssi, 0  # No filtering for unknown devices

                # Display the device information
                print(f"[Device] MAC: {device.address}, RSSI: {rssi}, UUIDs: {uuids}")
                if uuid in BEACONS:
                    print(f" → Filtered: {filtered_rssi:.2f} (±{error:.4f})")

                detected[device.address] = {
                    "uuids": uuids,
                    "rssi": rssi,
                    "filtered_rssi": filtered_rssi,
                    "error": error
                }

        print("[BLE] Detected devices:", detected)
        return detected

    except BleakError as e:
        print(f"[ERROR] BLE scanning failed: {e}")
        return {}

def ble_scan_thread():
    """Thread function for continuous BLE scanning."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    while True:
        detected = loop.run_until_complete(scan_by_mac())
        time.sleep(SCAN_INTERVAL)

# Start BLE scanning in a separate thread
ble_thread = threading.Thread(target=ble_scan_thread, daemon=True)
ble_thread.start()
