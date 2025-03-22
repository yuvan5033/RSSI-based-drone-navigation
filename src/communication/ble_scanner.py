import threading
import time

def ble_scan():
    while True:
        print("[BLE] Scanning for BLE beacons...")
        time.sleep(3)  # Placeholder for BLE scanning

if __name__ == "__main__":
    t = threading.Thread(target=ble_scan)
    t.start()
