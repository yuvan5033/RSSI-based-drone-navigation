import threading
import time

def gripper_control():
    while True:
        print("[Gripper] Activating gripper...")
        time.sleep(2)  # Placeholder for gripper operation

if __name__ == "__main__":
    t = threading.Thread(target=gripper_control)
    t.start()
