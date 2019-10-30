"""
Name: submenu.py
Author: Wesley Lee
Assignment: Visualization Project
Date Created: 11-02-2017
Last Updated: 11-23-2017

Description:
	Displays a specific chart based off of user choice.
"""

#!/usr/bin/python
import get_info, chart_choice, printer, data_options

# Displays a specific chart based off of the choice option
def chart_menu(token, url, port):
	printer.chart_menu_options()
	option = raw_input(printer.submenu)
	
	if option == '1':
		report_id = raw_input(printer.report_id)
		get_info.get_report(token, url, port, report_id, '4')
		data_options.data_option(option)
	
	elif option == '2':
		report_id = raw_input(printer.report_id)
		get_info.get_report(token, url, port, report_id, '5')
		data_options.data_option(option)
		
	elif option == '3':
		report_id = raw_input(printer.report_id)
		get_info.get_report(token, url, port, report_id, '6')
		data_options.data_option(option)
	
	elif option == '4':
		report_id = raw_input(printer.report_id)
		get_info.get_report(token, url, port, report_id, '7')
		data_options.data_option(option)
				
	elif option == '5':
		report_id = raw_input(printer.report_id)
		get_info.get_report(token, url, port, report_id, '8')
		data_options.data_option(option)
		
	elif option == '6':
		report_id = raw_input(printer.report_id)
		get_info.get_report(token, url, port, report_id, '9')
		chart_choice.stacked_bar()
		
	elif option == '7':
		report_id = raw_input(printer.report_id)
		get_info.get_report(token, url, port, report_id, '9')
		chart_choice.area_chart()
