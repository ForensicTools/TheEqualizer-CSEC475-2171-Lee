"""
Name: setup.py
Author: Wesley Lee
Assignment: Visualization Project
Date Created: 11-16-2017
Last Updated: 11-16-2017
"""

#!/usr/bin/python
import os, sys

def install_pymods():
	# Install Python Module
	os.system("clear")
	print "Installing Necessary Python Modules...\n\n"
	os.system("pip install -r requirements.txt")


# Install Plotly Account
def install_plotly(username, api_key):
	import plotly
	
	if len(api_key) < 20 or len(api_key) > 20:
		print "\nInvalid API Key!"
		corrected_api_key = raw_input("Enter Plotly API Key: ")
		install_plotly(username, corrected_api_key)
	else: 
		plotly.tools.set_credentials_file(username=username, api_key=api_key)

def run_program(user_input):
	if user_input == 'y':
		os.system("./The_Equalizer.py")
	elif user_input == 'n':
		os.system("clear")
		sys.exit()
	else:
		print "\nInvalid Input!"
		corrected_user_input = raw_input("Would you like to start The Equalizer? [y|n] ")
		run_program(corrected_user_input)

def main():
	install_pymods()
	
	print "Installing Plotly Account...\n\n"
	username = raw_input("\nEnter Plotly Username: ")
	api_key = raw_input("Enter Plotly API Key: ")
	install_plotly(username, api_key)
	
	os.system("clear")
	print "Installation Finished Done!\n"
	user_option = raw_input("Would you like to start The Equalizer? [y|n] ")
	run_program(user_option)

main()