import serial
import time

# Configure the serial port and baud rate
serial_port = '/dev/ttyACM0'  # Replace with your Arduino's serial port
baud_rate = 9600  # Must match the baud rate set in your Arduino code

try:
    # Open the serial connection
    ser = serial.Serial(serial_port, baud_rate, timeout=1)
    print(f"Connected to {serial_port} at {baud_rate} baud.")

    # Send data to Arduino
    message = "Hello, Arduino!\n"  # The message to send
    ser.write(message.encode('utf-8'))
    print(f"Sent: {message.strip()}")

    # Delay to ensure the data is sent
    time.sleep(2)

    # Read response from Arduino (if any)
    if ser.in_waiting > 0:
        response = ser.readline().decode('utf-8').strip()
        print(f"Received: {response}")

    # Close the serial connection
    ser.close()
    print("Serial port closed.")

except serial.SerialException as e:
    print(f"Error: {e}")

except Exception as e:
    print(f"Unexpected error: {e}")
