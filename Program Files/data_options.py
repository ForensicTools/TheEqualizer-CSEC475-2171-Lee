"""
Name: data_options.py
Author: Wesley Lee
Assignment: Visualization Project
Date Created: 11-03-2017
Last Updated: 11-05-2017
"""

#!/usr/bin/python
from chart_choice import basic_pie_chart, basic_bar_chart, basic_bubble_chart, basic_scatter_chart, line_plot_chart
import printer

def data_option(chart_type):
	printer.data_option_menu()
	
	option = raw_input(printer.data_menu)
	
	if chart_type == '1':
		basic_pie_chart(option)
	elif chart_type =='2':
		basic_bar_chart(option)
	elif chart_type == '3':
		basic_bubble_chart(option)
	elif chart_type == '4':
		basic_scatter_chart(option)
	elif chart_type == '5':
		line_plot_chart(option)
		
