#! /usr/bin/python

import hashlib

def checkSum(filename, algorithm):
	fileSum = hashlib.algorithm(open(filename,'rb').read()).hexdigest()
	print("The " + algorithm + " filesum of " + filename + " is: " + fileSum)
	print("\nPlease come back soon!")
	pass

try:
	print("Available Algorithms: md5, sha1, sha224, sha256, sha384, and sha512")
	filename = input("Filename: ")
	algorithm = input("Algorithm: ")
	checkSum(filename, algorithm)