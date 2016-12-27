#! /usr/bin/python3

import platform

if (platform.system() == "Windows"):
	file = input("Target File: ")
	mode = input("Handle Mode: (w, w+): ")
else:
	file = raw_input("Target File: ")
	mode = raw_input("Handle Mode: (w, w+): ")
	pass

def readFile(file, mode):
	handle = open(file, mode) # create a handle
	contents = handle.read() # put contents in a variable
	print(contents) # print out the contents
	handle.close # close the handle
	pass

if (mode != "w"):
	if (mode != "w+"):
			mode = "w+"
	pass
pass

readFile(file, mode)