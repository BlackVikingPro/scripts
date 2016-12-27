#!/usr/bin/python
import os
import platform

target_server = input("Domain or IP: ") #example

if (platform.system() == "Windows"):
	response = os.system("ping " + target_server + " -n 1")
	os.system("cls")
	pass

if (platform.system() == "Linux"):
	response = os.system("ping " + target_server + " -c 1")
	os.system("clear")
	pass

# and then check the response...
if response == 0:
	print(target_server + ' is up!')
else:
	print (target_server + ' is down! (it may just be your connection as well)')