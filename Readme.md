
# Arduino Serial Port Utility for Raspberry Pi

This repository contains utilities to detect, verify, and establish communication between an Arduino and a Raspberry Pi via a serial port. It includes:

- A Bash script to identify the serial port used by the Arduino.
- A Python script to test serial communication by sending and receiving acknowledgments.
- An Arduino sketch to test data exchange.

---

## Features

1. **Serial Port Detection**:
   - A Bash script (`Serial_Detect.sh`) that detects the port used by the Arduino when connected to the Raspberry Pi.

2. **Serial Communication Test**:
   - A Python script (`R2iConnect.py`) to verify communication by sending a message and receiving an acknowledgment.

3. **Arduino Sketch**:
   - A simple Arduino program (`transmitter.ino`) to handle serial communication, responding to messages from the Python script.

---

## Prerequisites

1. **Hardware**:
   - Raspberry Pi with available USB ports.
   - Arduino (Uno, Nano, or any compatible board).
   - USB cable to connect the Arduino to the Raspberry Pi.

2. **Software**:
   - Raspberry Pi running a Linux-based OS (e.g., Raspberry Pi OS).
   - Python 3.x installed on the Raspberry Pi.
   - `pyserial` library for Python (`pip install pyserial`).

---

## Usage

### 1. Detect Arduino's Serial Port

Run the Bash script to detect the serial port used by the Arduino:
```bash
bash Serial_Detect.sh
```

- Follow the prompts to connect and disconnect the Arduino.
- The script will output the detected port (e.g., `/dev/ttyUSB0`).

### 2. Verify Communication with Python

Update the serial port in `R2iConnect.py`:
```python
serial_port = '/dev/ttyUSB0'  # Replace with the detected port
```

Run the Python script to test communication:
```bash
python3 R2iConnect.py
```

- The script will send a test message to the Arduino and print any acknowledgment received.

### 3. Arduino Code

Upload the Arduino sketch (`transmitter.ino`) to your Arduino board using the Arduino IDE.

- This sketch listens for messages on the serial port and responds with an acknowledgment.

---

## Files in the Repository

- **`Serial_Detect.sh`**:
  Bash script to detect the serial port used by the Arduino.

- **`R2iConnect.py`**:
  Python script to send and receive messages via the detected serial port.

- **`transmitter.ino`**:
  Arduino sketch to handle serial communication with the Raspberry Pi.

---

## Example Output

### Detecting Serial Port
```bash
Please disconnect your Arduino and press Enter.
Now, connect your Arduino and press Enter.
Arduino is connected on port: /dev/ttyUSB0
```

### Running the Python Script
```bash
Connected to /dev/ttyUSB0 at 9600 baud.
Sent: Hello, Arduino!
Received: Hello from Arduino!
Serial port closed.
```

### Arduino Serial Monitor
```plaintext
Received: Hello, Arduino!
Reply sent: Hello from Arduino!
```

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

# Note
sudo apt install python3-pip
pip3 --version
pip install pyserial --break-system-packages
sudo apt update
sudo apt install python3-serial
