void setup() {
  Serial.begin(9600);  // Set baud rate
  while (!Serial) {
    ; // Wait for the serial port to initialize
  }
  Serial.println("Arduino is ready.");
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readString();  // Read data from serial
    Serial.print("Received: ");
    Serial.println(data);  // Print received data
    Serial.println("Hello from Arduino!");  // Send a response
  }
}
