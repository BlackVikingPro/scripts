#!/usr/bin/python
import getpass
import os

print("Signup!\n");
usr = input("Username: ");
pwd = getpass.getpass("Password: ");

print("Your username is: " + usr);
print("Your password is: " + pwd);
os.system("pause");