#!/usr/bin/env bash

# Get the game system name
system=$1

# Write SOLID to the text file
echo "SOLID" > $HOME/control.txt

# Call the solid colour Python code and pass the system name variable
sudo python /home/pi/Pimoroni/retroblinkt.py $system &
