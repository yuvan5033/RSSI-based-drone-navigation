import threading
import time
import yaml
import matplotlib.pyplot as plt
import random

# Load beacon coordinates from config
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

BEACONS = config["beacons"]

# Dummy RSSI values for visualization
rssi_values = {uuid: random.randint(-80, -40) for uuid in BEACONS.keys()}


def update_rssi():
    """Simulate RSSI values changing over time"""
    while True:
        for uuid in rssi_values:
            rssi_values[uuid] += random.randint(-2, 2)
            rssi_values[uuid] = max(-90, min(-40, rssi_values[uuid]))  # Keep values in range
        time.sleep(1)


def visualize_beacons():
    """Plot the beacon locations with dynamic RSSI values"""
    plt.ion()
    fig, ax = plt.subplots()

    while True:
        ax.clear()
        ax.set_title("BLE Beacons with RSSI Visualization")
        ax.set_xlabel("X Coordinate (m)")
        ax.set_ylabel("Y Coordinate (m)")

        for uuid, coords in BEACONS.items():
            x, y = coords["x"], coords["y"]
            rssi = rssi_values.get(uuid, -100)

            ax.scatter(x, y, color='blue', label=f"{uuid} ({rssi} dBm)")
            ax.text(x + 0.1, y + 0.1, f"RSSI: {rssi} dBm", fontsize=10)

        plt.draw()
        plt.pause(1)


if __name__ == "__main__":
    # Start RSSI updater thread
    t = threading.Thread(target=update_rssi)
    t.start()

    # Start visualizer
    visualize_beacons()
