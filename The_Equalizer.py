#!/usr/bin/python

import os

print """
What OS are you running?

1) MacOS
2) Linux
"""

os_choice = raw_input("OS Type: ")

if os_choice == '1':
	os.system("python Program\ Files/The_Equalizer.py")
elif os_choice == '2':
	os.system("python Program\ Files/The_Equalizer.py")