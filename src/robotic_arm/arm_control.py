import threading
import time

def arm_control():
    while True:
        print("[Arm] Moving to pick, hold, drop position...")
        time.sleep(4)  # Placeholder for PID-based movement

if __name__ == "__main__":
    t = threading.Thread(target=arm_control)
    t.start()
