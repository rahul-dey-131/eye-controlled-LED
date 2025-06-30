👁️ Eye-Controlled LED System using Computer Vision & Arduino
This project combines MediaPipe Face Mesh with Arduino to create a real-time eye detection system that controls an LED. When your eyes are open, the LED turns on; when closed, it turns off — all hands-free.

---

🔍 How It Works
- MediaPipe + OpenCV detects eye landmarks from webcam video.

- Calculates the distance between upper and lower eyelids to determine if eyes are open or closed.

- Uses an ultrasonic sensor (10–60 cm range) to adjust threshold dynamically based on the user's distance from the camera.

- Sends 1 (eyes open) or 0 (eyes closed) via serial communication to Arduino.

- Arduino receives the signal and controls an LED accordingly.

---

🛠️ Technologies Used

- Python (MediaPipe, OpenCV, PySerial)

- Arduino (Ultrasonic Sensor, LED, Breadboard, Jumpers, Webcam, Arduino Microcontroller)

- Serial Communication

---

📦 Files

- main.py: Python script for eye detection and serial communication.

- sonarData.ino: Arduino code to receive data and control the LED.
