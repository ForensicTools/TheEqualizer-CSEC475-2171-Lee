"""
Name: The_Equalizer.py
Author: Wesley Lee
Assignment: Visualization Project
Date Created: 11-02-2017
Last Updated: 11-05-2017
"""

#!/usr/bin/python
import os, sys
from create_token import create_token, get_token
from get_info import get_info, get_report, get_num_of_hosts, get_ips, get_crits, get_high, get_medium, get_low, get_score, get_total_vulnerabilities
from chart_choice import basic_pie_chart, basic_bar_chart, basic_bubble_chart, basic_scatter_chart, line_plot_chart
from submenu import chart_menu
from beautifultable import BeautifulTable

banner = """
 _____ _          _____             _ _             
|_   _| |_ ___   |   __|___ _ _ ___| |_|___ ___ ___ 
  | | |   | -_|  |   __| . | | | .'| | |- _| -_|  _|
  |_| |_|_|___|  |_____|_  |___|__,|_|_|___|___|_|  
		         |_|              
		               
	By Wesley Lee -- wtl5736@rit.edu   
=========================================================       
"""

menu = """================================================
1) Get Scanner Info
2) Print a specific report
3) Number of Vulnerabilities per IP from Scan
4) Graph a Chart

c) Clear Terminal
e) Exit Program
================================================
"""
			
def the_equalizer():
	os.system("clear")
	username = "VisProj" #raw_input("Username: ")
	password = "Password1234" #getpass.getpass()
	port = "8834" #raw_input("Port the server is running on: ")
	
	create_token(username, password, port)
	token = get_token()
	
	print banner
	
	while 1:
		print menu
		option = raw_input("The Equalizer> ")
		
		if option == 'c':
			os.system("clear")
			print banner
		
		elif option == 'e':
			os.system("rm -rf token.txt")
			os.system("rm -rf report.txt")
			sys.exit()
			
		elif option == '1':
			get_info(token, port, '2')
			option = raw_input("\n(press q to quit): ")
			
			while option != 'q':
				option = raw_input("\n(press q to quit): ")
			
			the_equalizer()
			
		elif option == '2':
			report_id = raw_input("Enter the Report ID: ")
			get_report(token, port, report_id, '2')
			option = raw_input("\n(press q to quit): ")
			
			while option != 'q':
				option = raw_input("\n(press q to quit): ")
			
			the_equalizer()
			
		elif option == '3':
			report_id = raw_input("Enter the Report ID: ")
			get_report(token, port, report_id, '3')
			
			ips = get_ips()
			vulns = get_total_vulnerabilities()
			table = BeautifulTable()
			table.column_headers = ("IP", "# of Vulnerabilities")
			
			print "\n"
			
			x = 0
			while x < len(ips):
				table.append_row([ips[x], vulns[x]])
				x += 1
			
			print table
			
			option = raw_input("\n(press q to quit): ")
			
			while option != 'q':
				option = raw_input("\n(press q to quit): ")
			
		elif option == '4':
			chart_menu(token, port)
		
		os.system("clear")
		print banner
			
	os.system("rm -rf token.txt")
	os.system("rm -rf report.txt")
			
the_equalizer()
