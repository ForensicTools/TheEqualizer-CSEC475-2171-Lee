"""
Name: data_options.py
Author: Wesley Lee
Assignment: Visualization Project
Date: 11-03-2017
"""

#!/usr/bin/python
from chart_choice import basic_pie_chart, basic_bar_chart, basic_bubble_chart, basic_scatter_chart, line_plot_chart

data_choice = """
================================================
1) Score
2) Total Vulnerabilities
3) Critical Vulnerabilities
4) High Vulnerabilities
5) Medium Vulnerabilities
6) Low Vulnerabilities
7) Info Vulnerabilities
================================================
"""

data_menu = "Data Option> "

def data_option(chart_type):
	print(data_choice)
	
	option = raw_input(data_menu)
	
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
		
