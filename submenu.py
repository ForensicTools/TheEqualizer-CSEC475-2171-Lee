"""
Name: submenu.py
Author: Wesley Lee
Assignment: Visualization Project
Date Created: 11-02-2017
Last Updated: 11-05-2017
"""

#!/usr/bin/python
from get_info import get_info, get_report, get_num_of_hosts, get_ips, get_crits, get_high, get_medium, get_low, get_score, get_info_vulns
from chart_choice import basic_pie_chart, basic_bar_chart, basic_bubble_chart, basic_scatter_chart, line_plot_chart, stacked_bar, area_chart
from data_options import data_option

chart_menu_options = """
================================================
1) Basic Pie Chart
2) Basic Bar Chart
3) Bubble Chart
4) Scatter Plot
5) Simple Line Plot
6) Stacked Bar Chart (Vulnerabilities Only)
7) Area Chart (Vulnerabilities Only)
================================================
"""

def chart_menu(token, port):
	print chart_menu_options
	option = raw_input("Graph a Chart> ")
	
	if option == '1':
		report_id = raw_input("Enter the Report ID: ")
		get_report(token, port, report_id, '4')
		data_option(option)
	
	elif option == '2':
		report_id = raw_input("Enter the Report ID: ")
		get_report(token, port, report_id, '5')
		data_option(option)
		
	elif option == '3':
		report_id = raw_input("Enter the Report ID: ")
		get_report(token, port, report_id, '6')
		data_option(option)
	
	elif option == '4':
		report_id = raw_input("Enter the Report ID: ")
		get_report(token, port, report_id, '7')
		data_option(option)
				
	elif option == '5':
		report_id = raw_input("Enter the Report ID: ")
		get_report(token, port, report_id, '8')
		data_option(option)
		
	elif option == '6':
		report_id = raw_input("Enter the Report ID: ")
		get_report(token, port, report_id, '9')
		stacked_bar()
		
	elif option == '7':
		report_id = raw_input("Enter the Report ID: ")
		get_report(token, port, report_id, '9')
		area_chart()
