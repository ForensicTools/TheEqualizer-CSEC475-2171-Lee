#!/usr/bin/python
import os, sys
from create_token import create_token, get_token
from get_info import get_info, get_report, get_num_of_hosts, get_ips, get_crits, get_high, get_medium, get_low, get_score
from chart_choice import print_stuff, basic_pie_chart, basic_bar_chart, basic_bubble_chart, basic_scatter_chart, line_plot_chart


banner = """
 _____ _          _____             _ _             
|_   _| |_ ___   |   __|___ _ _ ___| |_|___ ___ ___ 
  | | |   | -_|  |   __| . | | | .'| | |- _| -_|  _|
  |_| |_|_|___|  |_____|_  |___|__,|_|_|___|___|_|  
		         |_|                                
=========================================================       
"""

menu = """==============================
1) Get Scanner Info
2) Print a specific report
3) TBD
4) Basic Pie Chart of Scan (IPs and Score)
5) Basic Bar Chart of Scan (IPs and Score)
6) Bubble Chart of Scan (IPs and Score)
7) Scatter Plot of Scan (IPs and Score)
8) Simple Line Plot of Scan (IPs and Score)

c) Clear Terminal
e) Exit Program
==============================
"""
			
def main():
	os.system("clear")
	print(banner)
	username = "VisProj" #raw_input("Username: ")
	password = "Password1234" #getpass.getpass()
	port = "8834" #raw_input("Port the server is running on: ")
	
	create_token(username, password, port)
	token = get_token()
	
	while 1:
		print menu
		option = raw_input("The Equalizer> ")
		
		if option == 'c':
			os.system("clear")
			print(banner)
		
		elif option == 'e':
			os.system("rm -rf token.txt")
			os.system("rm -rf report.txt")
			sys.exit()
			
		elif option == '1':
			get_info(token, port)
			
		elif option == '2':
			report_id = raw_input("Enter the Report ID: ")
			get_report(token, port, report_id, '2')
			print("\n")
			
		elif option == '3':
			report_id = raw_input("Enter the Report ID: ")
			get_report(token, port, report_id, '3')
			print_stuff()
			#num_of_hosts = get_score()
			#print("\nThere was/were " + str(num_of_hosts[:]) + " host(s) scanned\n")
			
		elif option == '4':
			report_id = raw_input("Enter the Report ID: ")
			get_report(token, port, report_id, '4')
			basic_pie_chart()
			print("\n")	
		
		elif option == '5':
			report_id = raw_input("Enter the Report ID: ")
			get_report(token, port, report_id, '5')
			basic_bar_chart()
			print("\n")	
			
		elif option == '6':
			report_id = raw_input("Enter the Report ID: ")
			get_report(token, port, report_id, '6')
			basic_bubble_chart()
			print("\n")	
		
		elif option == '7':
			report_id = raw_input("Enter the Report ID: ")
			get_report(token, port, report_id, '7')
			basic_scatter_chart()
			print("\n")	
			
		elif option == '8':
			report_id = raw_input("Enter the Report ID: ")
			get_report(token, port, report_id, '8')
			line_plot_chart()
			print("\n")	

main()