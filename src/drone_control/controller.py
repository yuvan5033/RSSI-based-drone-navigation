import threading
import time

def drone_controller():
    while True:
        print("[Drone] Navigating using PID/LQR...")
        time.sleep(2)  # Placeholder for PID loop execution

if __name__ == "__main__":
    t = threading.Thread(target=drone_controller)
    t.start()
