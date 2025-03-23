#### **RSSI-Based Autonomous Drone Navigation for Garbage Collection Using Control Systems**

---

### 🛠️ **Project Overview**

This project implements an autonomous drone navigation system controlled by a Raspberry Pi, utilizing RSSI signals from BLE beacons to locate garbage bins. The drone uses a camera for trash detection and a robotic arm to pick up and dispose of garbage into the bins.

---

### 🔥 **Features**

- **RSSI-Based Navigation:**

  - The drone uses RSSI signals from BLE beacons to navigate to the closest garbage bin.
  - Kalman filtering smoothens signal noise.
  - PID or LQR control system ensures stable movement.

- **Trash Detection:**

  - Onboard camera detects trash on the ground using object detection models.

- **Garbage Collection:**

  - The robotic arm performs **pick-hold-drop** actions.
  - PID-controlled movement ensures precise gripping and dropping.

- **Communication:**
  - BLE for beacon detection.
  - MQTT for data exchange between the drone and Raspberry Pi.

---

### 📁 **Project Structure**

```
/rssi-drone-nav
├── /src
│   ├── /drone_control           # Navigation & control logic
│   │   ├── __init__.py
│   │   ├── controller.py        # PID/LQR navigation control
│   │   ├── rssi_navigation.py   # RSSI beacon tracking
│   │   └── kalman_filter.py     # Noise reduction
│   │
│   ├── /robotic_arm             # Arm for garbage pickup
│   │   ├── __init__.py
│   │   ├── arm_control.py       # Pick, hold, drop PID
│   │   └── gripper.py           # Gripper logic
│   │
│   ├── /vision                  # Trash detection
│   │   ├── __init__.py
│   │   ├── camera.py            # Camera feed handling
│   │   └── object_detection.py  # Trash detection
│   │
│   ├── /communication           # Drone-RPi communication
│   │   ├── __init__.py
│   │   ├── mqtt_client.py       # MQTT data exchange
│   │   └── ble_scanner.py       # BLE beacon scanning
│
├── /data                        # Logs & telemetry
│   ├── flight_log.csv
│   ├── rssi_log.csv
│   └── telemetry.csv
│
├── main.py                       # Main entry point
├── requirements.txt              # Python dependencies
├── config.yaml                   # Configuration settings
└── README.md                     # Project overview
```

---

### 🛠️ **Installation & Setup**

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/rssi-drone-nav.git
cd rssi-drone-nav
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Modify Configuration:**

- Edit the `config.yaml` file with BLE beacon IDs and RSSI threshold values.

---

### 🚀 **Usage**

1. **Start the RSSI-based navigation system:**

```bash
python main.py
```

2. **Drone Navigation:**

   - The drone will scan for BLE beacons.
   - It will navigate to the closest bin using PID or LQR control.

3. **Trash Detection & Collection:**
   - The camera detects trash on the ground.
   - The robotic arm picks and disposes of garbage into the bin.

---

### 🔥 **Technologies Used**

- **Raspberry Pi** – Drone control & BLE scanning
- **Python** – Control system, navigation, and image processing
- **OpenCV** – Trash detection
- **MQTT** – Communication protocol
- **PID/LQR Control** – Precision navigation
- **BLE Beacons** – RSSI-based localization

---

### 📊 **Data Logs**

- **RSSI Logs:** `rssi_log.csv` – Stores beacon signals and distances.
- **Flight Logs:** `flight_log.csv` – Contains navigation data.
- **Telemetry:** `telemetry.csv` – Captures telemetry data for debugging.

---

### ⚙️ **Configuration**

`config.yaml` – Configuration file for system parameters:

```yaml
beacon_ids:
  - "00:11:22:33:44:55"
  - "AA:BB:CC:DD:EE:FF"

rssi_threshold: -70 # RSSI threshold for beacon proximity
pid:
  kp: 1.2
  ki: 0.5
  kd: 0.05
```

---

### ⚠️ **Troubleshooting**

- **Weak BLE signal:**
  - Ensure the beacons are within range.
- **Inconsistent navigation:**
  - Tune the PID parameters in `config.yaml`.
- **Trash detection accuracy:**
  - Adjust the detection threshold in `object_detection.py`.

---

### 👨‍💻 **Contributors**

- [Yuvan Reddy](https://github.com/yuvan5033)

---

### ⭐ **Future Enhancements**

- Integrate SLAM for better navigation.
- Implement real-time obstacle avoidance.
- Add LiDAR for more precise navigation.
