import threading
import time

def mqtt_publish():
    while True:
        print("[MQTT] Publishing drone telemetry...")
        time.sleep(2)  # Placeholder for publishing

if __name__ == "__main__":
    t = threading.Thread(target=mqtt_publish)
    t.start()
