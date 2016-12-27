#!/usr/bin/env bash

# Created by: BlackVikingPro.
# official.blackvikingpro@gmail.com

read -p "New Mac Address? " new_mac
clear
ifconfig
echo "Please search for the Interphase you'd like to spoof."
read -p "Chosen Interphase? " interphase
# now let's start the spoof
sudo ip link set dev $interphase down
sudo ip link set dev $interphase address $new_mac
sudo ip link set dev $interphase up
clear
echo "Done! Below is your new Mac Address!"
ip link show $interphase