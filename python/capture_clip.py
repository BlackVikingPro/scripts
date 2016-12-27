#!/usr/bin/python

import os
import random
import ftplib
from tkinter import Tk

# now, we will grab all Windows clipboard data, and put to var
clipboard = Tk().clipboard_get()

random_num = random.randrange(100, 1000, 2)
random_num_2 = random.randrange(1, 9999, 5)
filename = "capture_clip" + str(random_num) + str(random_num_2)
file = open(filename, 'w') # clears file, or create if not exist
file.write(clipboard) # write all contents of var "foo" to file
file.close() # close file after printing