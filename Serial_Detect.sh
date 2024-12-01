#!/bin/bash

# Detect the Arduino USB port
echo "Please disconnect your Arduino and press Enter."
read -r  # Wait for user confirmation

# Capture the list of devices before Arduino is connected
devices_before=$(ls /dev/tty* 2>/dev/null)

echo "Now, connect your Arduino and press Enter."
read -r  # Wait for user confirmation

# Capture the list of devices after Arduino is connected
devices_after=$(ls /dev/tty* 2>/dev/null)

# Compare the two lists and find the new port
new_device=$(comm -13 <(echo "$devices_before" | sort) <(echo "$devices_after" | sort))

if [[ -z $new_device ]]; then
  echo "No new device detected. Make sure the Arduino is properly connected."
else
  echo "Arduino is connected on port: $new_device"
fi
