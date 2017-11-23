#!/usr/bin/python

import os

print """
What OS are you running?

1) Windows
2) MacOS
3) Linux
"""

os = raw_input("OS Type: ")

if os == '1':
	os.system("python \"Program Files\The_Equalizer.py\"")
elif os == '2':
	os.system("python Program\ Files/The_Equalizer.py")
elif os == '3':
	os.system("python Program\ Files/The_Equalizer.py")