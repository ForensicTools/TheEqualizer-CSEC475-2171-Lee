"""
Name: The_Equalizer.py
Author: Wesley Lee
Assignment: Visualization Project
Date Created: 11-02-2017
Last Updated: 11-23-2017

Description:
	Runs the Main Program.
"""

#!/usr/bin/python
import os

os.system("clear")

print """What OS are you running?

1) MacOS
2) Linux
"""

os_choice = raw_input("OS Type: ")

# OS Specification
if os_choice == '1':
	os.system("osascript StyleTerm.scpt 1 Homebrew")
	os.system("python Program\ Files/Main.py")
	
elif os_choice == '2':
	os.system("python Program\ Files/Main.py")