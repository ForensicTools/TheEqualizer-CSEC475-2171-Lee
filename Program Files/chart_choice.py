"""
Name: chart_choice.py
Author: Wesley Lee
Assignment: Visualization Project
Date Created: 11-02-2017
Last Updated: 11-23-2017

Description:
	Graphs a chart with data option specified by user.
"""

#!/usr/bin/python
import get_info, graphs 

# Graphs a basic pie chart with data specified by user
def basic_pie_chart(data_option):
	ips = get_info.get_ips()
	if data_option == '1':
		score = get_info.get_score()
		graphs.pie_chart(ips, score)
	elif data_option == '2':
		total_vuln = get_info.get_total_vulnerabilities()
		graphs.pie_chart(ips, total_vuln)
	elif data_option == '3':
		crits = get_crits()
		graphs.pie_chart(ips, crits)
	elif data_option == '4':
		high_vuln = get_info.get_high()
		graphs.pie_chart(ips, high_vuln)
	elif data_option == '5':
		medium_vuln = get_info.get_medium()
		graphs.pie_chart(ips, medium_vuln)
	elif data_option == '6':
		low_vuln = get_info.get_low()
		graphs.pie_chart(ips, low_vuln)
	elif data_option == '7':
		info_vuln == get_info.get_info_vulns()
		graphs.pie_chart(ips, info_vuln)

# Graphs a basic bar chart with data specified by user
def basic_bar_chart(data_option):
	ips = get_info.get_ips()
	if data_option == '1':
		score = get_info.get_score()
		graphs.bar_chart(ips, score)
	elif data_option == '2':
		total_vuln = get_info.get_total_vulnerabilities()
		graphs.bar_chart(ips, total_vuln)
	elif data_option == '3':
		crits = get_info.get_crits()
		graphs.bar_chart(ips, crits)
	elif data_option == '4':
		high_vuln = get_info.get_high()
		graphs.bar_chart(ips, high_vuln)
	elif data_option == '5':
		medium_vuln = get_info.get_medium()
		graphs.bar_chart(ips, medium_vuln)
	elif data_option == '6':
		low_vuln = get_info.get_low()
		graphs.bar_chart(ips, low_vuln)
	elif data_option == '7':
		info_vuln == get_info.get_info_vulns()
		graphs.bar_chart(ips, info_vuln)

# Graphs a bubble chart with data specified by user	
def basic_bubble_chart(data_option):
	ips = get_info.get_ips()
	if data_option == '1':
		score = get_info.get_score()
		graphs.bubble_chart(ips, score)
	elif data_option == '2':
		total_vuln = get_info.get_total_vulnerabilities()
		graphs.bubble_chart(ips, total_vuln)
	elif data_option == '3':
		crits = get_info.get_crits()
		graphs.bubble_chart(ips, crits)
	elif data_option == '4':
		high_vuln = get_info.get_high()
		graphs.bubble_chart(ips, high_vuln)
	elif data_option == '5':
		medium_vuln = get_info.get_medium()
		graphs.bubble_chart(ips, medium_vuln)
	elif data_option == '6':
		low_vuln = get_info.get_low()
		graphs.bubble_chart(ips, low_vuln)
	elif data_option == '7':
		info_vuln == get_info.get_info_vulns()
		graphs.bubble_chart(ips, info_vuln)

# Graphs a scatter plot with data specified by user
def basic_scatter_chart(data_option):
	ips = get_info.get_ips()
	if data_option == '1':
		score = get_info.get_score()
		graphsscatter_plot(ips, score)
	elif data_option == '2':
		total_vuln = get_info.get_total_vulnerabilities()
		graphs.scatter_plot(ips, total_vuln)
	elif data_option == '3':
		crits = get_info.get_crits()
		graphs.scatter_plot(ips, crits)
	elif data_option == '4':
		high_vuln = get_info.get_high()
		graphs.scatter_plot(ips, high_vuln)
	elif data_option == '5':
		medium_vuln = get_info.get_medium()
		graphs.scatter_plot(ips, medium_vuln)
	elif data_option == '6':
		low_vuln = get_info.get_low()
		graphs.scatter_plot(ips, low_vuln)
	elif data_option == '7':
		info_vuln == get_info_vulns()
		graphs.scatter_plot(ips, info_vuln)

# Graphs a line plot with data specified by user	
def line_plot_chart(data_option):
	ips = get_info.get_ips()
	if data_option == '1':
		score = get_info.get_score()
		graphs.simple_line_plot(ips, score)
	elif data_option == '2':
		total_vuln = get_info.get_total_vulnerabilities()
		graphs.simple_line_plot(ips, total_vuln)
	elif data_option == '3':
		crits = get_info.get_crits()
		graphs.simple_line_plot(ips, crits)
	elif data_option == '4':
		high_vuln = get_info.get_high()
		graphs.simple_line_plot(ips, high_vuln)
	elif data_option == '5':
		medium_vuln = get_info.get_medium()
		graphs.simple_line_plot(ips, medium_vuln)
	elif data_option == '6':
		low_vuln = get_info.get_low()
		graphs.simple_line_plot(ips, low_vuln)
	elif data_option == '7':
		info_vuln = get_info.get_info_vulns()
		graphs.simple_line_plot(ips, info_vuln)

# Graphs a stacked bar chart with data specified by user		
def stacked_bar():
	ips = get_info.get_ips()
	crits = get_info.get_crits()
	high = get_info.get_high()
	medium = get_info.get_medium()
	low = get_info.get_low()
	
	graphs.stacked_bar_chart(ips, crits, high, medium, low)

# Graphs a area chart with data specified by user	
def area_chart():
	ips = get_info.get_ips()
	crits = get_info.get_crits()
	high = get_info.get_high()
	medium = get_info.get_medium()
	low = get_info.get_low()
	
	graphs.stacked_area_chart(ips, crits, high, medium, low)
	