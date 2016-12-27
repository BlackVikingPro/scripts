#!/usr/bin/python3

# Change MAC Address | By: BlackVikingPro

import os

interphase = raw_input("Target Interphase: ");
print("\nExample MAC Address: 1a:2b:3c:4d:5e:6f");
print("Leave MAC Address field blank for default Anonymous MAC Address (1a:2b:3c:4d:5e:6f)");
new_mac = raw_input("New MAC Address: ");

def change_mac(interphase, new_mac):
	if (new_mac == ""):
		new_mac = "1a:2b:3c:4d:5e:6f"
		pass
	os.system("sudo ip link set dev " + interphase + " down"); # Shut this interphase down.
	os.system("sudo ip link set dev " + interphase + " address " + new_mac); # change the mac address
	os.system("sudo ip link set dev " + interphase + " up"); # restart the interphase
	pass

change_mac(interphase, new_mac);