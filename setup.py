"""
Name: setup.py
Author: Wesley Lee
Assignment: Visualization Project
Date Created: 11-16-2017
Last Updated: 11-23-2017

Description:
	Installs Requirements and Sets up plotly accounts.
"""

#!/usr/bin/python
import os, sys
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, BOLD, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[1m', '\033[0m'

def os_choice():
	print """What OS are you running?

	1) MacOS
	2) Linux
	"""
	os_choice = raw_input("OS Type: ")
	
	if os_choice == '1':
		install_pymods_macos()
	elif os_choice == '2':
		install_pymods_linux()

# Installs required python modules
def install_pymods_macos():
	# Install Python Module
	os.system("clear")
	print "Installing Necessary Python Modules...\n\n"
	os.system("pip install -r requirements.txt")

def install_pymods_linux():
	# Install Python Module
	os.system("clear")
	print "Installing pip for Python...\n"
	os.system("apt-get install python-pip -y")
	os.system("pip install --upgrade pip")
	
	print "\nInstalling curl...\n"
		os.system("apt-get install curl")
	
	print "\nInstalling Necessary Python Modules...\n\n"
	os.system("pip install -r requirements.txt")

def is_root():
	if not os.geteuid()==0:
		print("\n{0}ERROR: setup.py must be run with root privileges. Try again with sudo:\n\t{1}$ sudo python setup.py{2}\n").format(RED, GREEN, END)
		sys.exit()

# Install Plotly Account
def install_plotly(username, api_key):
	import plotly
	
	if len(api_key) < 20 or len(api_key) > 20:
		print "\nInvalid API Key!"
		corrected_api_key = raw_input("Enter Plotly API Key: ")
		install_plotly(username, corrected_api_key)
	else: 
		plotly.tools.set_credentials_file(username=username, api_key=api_key)

# Run The Equalizer Program
def run_program(user_input):
	if user_input == 'y':
		os.system("python The_Equalizer.py")
	elif user_input == 'n':
		os.system("clear")
		sys.exit()
	else:
		print "\nInvalid Input!"
		corrected_user_input = raw_input("Would you like to start The Equalizer? [y|n] ")
		run_program(corrected_user_input)

# Main to run all everything
def main():
	is_root()
	os_choice()
	
	print "Installing Plotly Account...\n\n"
	username = raw_input("\nEnter Plotly Username: ")
	api_key = raw_input("Enter Plotly API Key: ")
	install_plotly(username, api_key)
	
	os.system("clear")
	print "Installation Finished Done!\n"
	user_option = raw_input("Would you like to start The Equalizer? [y|n] ")
	run_program(user_option)
	
	
if __name__ == "__main__":
	main()
