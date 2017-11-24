"""
Name: data_options.py
Author: Wesley Lee
Assignment: Visualization Project
Date Created: 11-03-2017
Last Updated: 11-23-2017

Description:
	Graphs the chart with the data option
	chosen by the user.
"""

#!/usr/bin/python
import chart_choice, printer

# Data Option Specification
def data_option(chart_type):
	printer.data_option_menu()
	
	option = raw_input(printer.data_menu)
	
	if chart_type == '1':
		chart_choice.basic_pie_chart(option)
	elif chart_type =='2':
		chart_choice.basic_bar_chart(option)
	elif chart_type == '3':
		chart_choice.basic_bubble_chart(option)
	elif chart_type == '4':
		chart_choice.basic_scatter_chart(option)
	elif chart_type == '5':
		chart_choice.line_plot_chart(option)
		
