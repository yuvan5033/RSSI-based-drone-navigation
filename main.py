import threading
from src.drone_control.controller import drone_controller
from src.drone_control.rssi_navigation import rssi_navigation
from src.robotic_arm.arm_control import arm_control
from src.robotic_arm.gripper import gripper_control
from src.vision.camera import camera_feed
from src.vision.object_detection import detect_trash
from src.communication.mqtt_client import mqtt_publish
from src.communication.ble_scanner import ble_scan_thread

def main():
    print("[System] Starting drone navigation system...")

    # Multithreading setup
    threads = [
        #threading.Thread(target=drone_controller),
        #threading.Thread(target=rssi_navigation),
        #threading.Thread(target=arm_control),
        #threading.Thread(target=gripper_control),
        #threading.Thread(target=camera_feed),
        #threading.Thread(target=detect_trash),
        #threading.Thread(target=mqtt_publish),
        threading.Thread(target=ble_scan_thread),
    ]

    # Start all threads
    for t in threads:
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
