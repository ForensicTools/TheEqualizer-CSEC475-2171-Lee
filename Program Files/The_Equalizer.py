"""
Name: The_Equalizer.py
Author: Wesley Lee
Assignment: Visualization Project
Date Created: 11-02-2017
Last Updated: 11-16-2017
"""

#!/usr/bin/python
import os, sys
from create_token import create_token, get_token
from get_info import get_username, get_password, get_url, get_port, get_info, get_report, get_num_of_hosts, get_ips, get_crits, get_high, get_medium, get_low, get_score, get_total_vulnerabilities
from chart_choice import basic_pie_chart, basic_bar_chart, basic_bubble_chart, basic_scatter_chart, line_plot_chart
from submenu import chart_menu
import printer
from beautifultable import BeautifulTable
import getpass
	
def the_equalizer(url, port):
	try:	
		os.system("clear")
		printer.banner()
		
	except KeyboardInterrupt:
		os.system("clear")
		os.system("rm -rf token.txt")
		os.system("rm -rf report.txt")
		sys.exit()
	
	while True:
		
		try:
			while True:
				printer.print_main_menu()
				option = raw_input(printer.header)
				
				if option == 'c' or option == 'C':
					os.system("clear")
					printer.banner()
				
				elif option == 'e' or option == 'E':
					os.system("rm -rf token.txt")
					os.system("rm -rf report.txt")
					sys.exit()
					
				elif option == '1':
					get_info(token, url, port, '2')
					option = raw_input("\n(press q to quit): ")
					
					while option != 'q':
						option = raw_input("\n(press q to quit): ")
					
					the_equalizer(url, port)
					
				elif option == '2':
					report_id = raw_input(printer.report_id)
					get_report(token, url, port, report_id, '2')
					option = raw_input("\n(press q to quit): ")
					
					while option != 'q':
						option = raw_input("\n(press q to quit): ")
					
					the_equalizer(url, port)
					
				elif option == '3':
					report_id = raw_input(printer.report_id)
					get_report(token, url, port, report_id, '3')
					
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
					chart_menu(token, url, port)
					
				os.system("clear")
				printer.banner()
			
		except KeyboardInterrupt:
			os.system("clear")
			os.system("rm -rf token.txt")
			os.system("rm -rf report.txt")
			sys.exit()
		
		
if __name__ == "__main__":
	un = get_username()
	pw = get_password()
	url = get_url()
	port = get_port()
	
	create_token(un, pw, url, port)
	token = get_token()
	
	the_equalizer(url, port)
