import threading
import time

def camera_feed():
    while True:
        print("[Camera] Capturing images...")
        time.sleep(3)  # Placeholder for image capture

if __name__ == "__main__":
    t = threading.Thread(target=camera_feed)
    t.start()
