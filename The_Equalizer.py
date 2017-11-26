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
import os, sys
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, BOLD, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[1m', '\033[0m'

if not os.geteuid()==0:
	print("\n{0}ERROR: The Equalizer must be run with root privileges. Try again with sudo:\n\t{1}$ sudo python The_Equalizer.py{2}\n").format(RED, GREEN, END)
	sys.exit()

os.system("clear")

print """What OS are you running?

1) MacOS
2) Linux
"""

os_choice = raw_input("OS Type: ")

# OS Specification
if os_choice == '1':
	os.system("osascript StyleTerm.scpt 1 Homebrew")
	os.system("sudo python Program\ Files/Main.py")
	
elif os_choice == '2':
	os.system("sudo python Program\ Files/Main.py")