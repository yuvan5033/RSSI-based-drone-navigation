import threading
import time

def rssi_navigation():
    while True:
        print("[RSSI] Scanning for BLE beacons...")
        time.sleep(3)  # Placeholder for RSSI scanning

if __name__ == "__main__":
    t = threading.Thread(target=rssi_navigation)
    t.start()
