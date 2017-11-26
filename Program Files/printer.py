"""
Name: printer.py
Author: Wesley Lee
Assignment: Visualization Project
Date Created: 11-16-2017
Last Updated: 11-23-2017

Description:
	Prints all the necessary menus and banner when called.
"""

#!/usr/bin/python
import os, time

# Color Variables
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, BOLD, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[1m', '\033[0m'

# Main Text
header = (BOLD + '{0}The Equalizer{1}> {2}'.format(BLUE, WHITE, END))
submenu = (BOLD + '{0}Graph a Chart{1}> {2}'.format(BLUE, WHITE, END))
report_id = (BOLD + '{0}Enter the Report ID: {1}> {2}'.format(BLUE, WHITE, END))
data_menu = (BOLD + '{0}Data Option{1}> {2}'.format(BLUE, WHITE, END))

# The Equalizer Main Menu
def print_main_menu():
	print(BOLD + 'Choose option from menu:\n')
	sleeper()
	print('\t{0}[{1}1{2}]{3} Get Nessus Server Info').format(YELLOW, RED, YELLOW, WHITE)
	sleeper()
	print('\t{0}[{1}2{2}]{3} Display a Nessus Report').format(YELLOW, RED, YELLOW, WHITE)
	sleeper()
	print('\t{0}[{1}3{2}]{3} Display the Number of Vulnerabilities per IP/Hostname from Nessus Report').format(YELLOW, RED, YELLOW, WHITE)
	sleeper()
	print('\t{0}[{1}4{2}]{3} Graph a Nessus Report Data').format(YELLOW, RED, YELLOW, WHITE)
	sleeper()
	print('\n\t{0}[{1}C{2}]{3} Clear Terminal').format(YELLOW, RED, YELLOW, WHITE)
	sleeper()
	print('\t{0}[{1}E{2}]{3} Exit Program\n').format(YELLOW, RED, YELLOW, WHITE)
	
# Graph Menu Options
def chart_menu_options():
	print(BOLD + WHITE + '\nChoose a chart type:\n')
	sleeper()
	print('\t{0}[{1}1{2}]{3} Basic Pie Chart').format(YELLOW, RED, YELLOW, WHITE)
	sleeper()
	print('\t{0}[{1}2{2}]{3} Basic Bar Chart').format(YELLOW, RED, YELLOW, WHITE)
	sleeper()
	print('\t{0}[{1}3{2}]{3} Bubble Chart').format(YELLOW, RED, YELLOW, WHITE)
	sleeper()
	print('\t{0}[{1}4{2}]{3} Scatter Plot').format(YELLOW, RED, YELLOW, WHITE)
	sleeper()
	print('\t{0}[{1}5{2}]{3} Simple Line Plot').format(YELLOW, RED, YELLOW, WHITE)
	sleeper()
	print('\t{0}[{1}6{2}]{3} Stacked Bar Chart (Vulnerabilities Only)').format(YELLOW, RED, YELLOW, WHITE)
	sleeper()
	print('\t{0}[{1}7{2}]{3} Area Chart (Vulnerabilities Only)').format(YELLOW, RED, YELLOW, WHITE)
	sleeper()
	print(END)

# Data Options Menu
def data_option_menu():
	print(BOLD + WHITE + '\nChoose a data option:\n')
	sleeper()
	print('\t{0}[{1}1{2}]{3} Score').format(YELLOW, RED, YELLOW, WHITE)
	sleeper()
	print('\t{0}[{1}2{2}]{3} Total Vulnerabilities').format(YELLOW, RED, YELLOW, WHITE)
	sleeper()
	print('\t{0}[{1}3{2}]{3} Critical Vulnerabilities').format(YELLOW, RED, YELLOW, WHITE)
	sleeper()
	print('\t{0}[{1}4{2}]{3} High Vulnerabilities').format(YELLOW, RED, YELLOW, WHITE)
	sleeper()
	print('\t{0}[{1}5{2}]{3} Medium Vulnerabilities').format(YELLOW, RED, YELLOW, WHITE)
	sleeper()
	print('\t{0}[{1}6{2}]{3} Low Vulnerabilities').format(YELLOW, RED, YELLOW, WHITE)
	sleeper()
	print('\t{0}[{1}7{2}]{3} Info Vulnerabilities').format(YELLOW, RED, YELLOW, WHITE)
	sleeper()
	print(END)

# Function to display the menus faster
def sleeper():
	time.sleep(0)

# The Equalizer Banner
def banner():
	spaces = " " * 76
	print(BOLD + RED + spaces + """
 _____ _          _____             _ _             
|_   _| |_ ___   |   __|___ _ _ ___| |_|___ ___ ___ 
  | | |   | -_|  |   __| . | | | .'| | |- _| -_|  _|
  |_| |_|_|___|  |_____|_  |___|__,|_|_|___|___|_|  
		         |_|              
		               
	By Wesley Lee -- wtl5736@rit.edu     
=========================================================                                               """ + END + WHITE)