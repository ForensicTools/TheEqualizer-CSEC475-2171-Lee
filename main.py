#!/usr/bin/python

from create_token import create_token
from create_token import get_token
from get_info import get_info
from get_info import get_report
import os

banner = """
 _____ _          _____             _ _             
|_   _| |_ ___   |   __|___ _ _ ___| |_|___ ___ ___ 
  | | |   | -_|  |   __| . | | | .'| | |- _| -_|  _|
  |_| |_|_|___|  |_____|_  |___|__,|_|_|___|___|_|  
		         |_|                                
=========================================================       
"""

menu = """========================
1) Get Scanner Info
2) Print a specific report
3) TBD
========================
"""
			
def main():
	username = "VisProj"#raw_input("Username: ")
	password = "Password1234"#getpass.getpass()
	port = "8834"#raw_input("Port the server is running on: ")
	
	print(banner)
	create_token(username, password, port)
	token = get_token()
	
	while 1:
		print menu
		option = raw_input("The Equalizer> ")
		
		if option == '1':
			get_info(token, port)
			
		elif option == '2':
			report_id = raw_input("Enter the Report ID: ")
			get_report(token, port, report_id)
			print("\n")
			
			
	
	
main()