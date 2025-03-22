import threading
import time

def detect_trash():
    while True:
        print("[Detection] Identifying trash on ground plane...")
        time.sleep(5)  # Placeholder for detection processing

if __name__ == "__main__":
    t = threading.Thread(target=detect_trash)
    t.start()
