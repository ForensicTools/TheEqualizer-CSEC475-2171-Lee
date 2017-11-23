"""
Name: chart_choice.py
Author: Wesley Lee
Assignment: Visualization Project
Date Created: 11-02-2017
Last Updated: 11-16-2017
"""

#!/usr/bin/python
from get_info import get_info, get_report, get_num_of_hosts, get_ips, get_crits, get_high, get_medium, get_low, get_score, get_info_vulns, get_total_vulnerabilities
from graphs import pie_chart, bar_chart, bubble_chart, scatter_plot, simple_line_plot, stacked_bar_chart, stacked_area_chart

def basic_pie_chart(data_option):
	ips = get_ips()
	if data_option == '1':
		score = get_score()
		pie_chart(ips, score)
	elif data_option == '2':
		total_vuln = get_total_vulnerabilities()
		pie_chart(ips, total_vuln)
	elif data_option == '3':
		crits = get_crits()
		pie_chart(ips, crits)
	elif data_option == '4':
		high_vuln = get_high()
		pie_chart(ips, high_vuln)
	elif data_option == '5':
		medium_vuln = get_medium()
		pie_chart(ips, medium_vuln)
	elif data_option == '6':
		low_vuln = get_low()
		pie_chart(ips, low_vuln)
	elif data_option == '7':
		info_vuln == get_info_vulns()
		pie_chart(ips, info_vuln)
	
def basic_bar_chart(data_option):
	ips = get_ips()
	if data_option == '1':
		score = get_score()
		bar_chart(ips, score)
	elif data_option == '2':
		total_vuln = get_total_vulnerabilities()
		bar_chart(ips, total_vuln)
	elif data_option == '3':
		crits = get_crits()
		bar_chart(ips, crits)
	elif data_option == '4':
		high_vuln = get_high()
		bar_chart(ips, high_vuln)
	elif data_option == '5':
		medium_vuln = get_medium()
		bar_chart(ips, medium_vuln)
	elif data_option == '6':
		low_vuln = get_low()
		bar_chart(ips, low_vuln)
	elif data_option == '7':
		info_vuln == get_info_vulns()
		bar_chart(ips, info_vuln)
	
def basic_bubble_chart(data_option):
	ips = get_ips()
	if data_option == '1':
		score = get_score()
		bubble_chart(ips, score)
	elif data_option == '2':
		total_vuln = get_total_vulnerabilities()
		bubble_chart(ips, total_vuln)
	elif data_option == '3':
		crits = get_crits()
		bubble_chart(ips, crits)
	elif data_option == '4':
		high_vuln = get_high()
		bubble_chart(ips, high_vuln)
	elif data_option == '5':
		medium_vuln = get_medium()
		bubble_chart(ips, medium_vuln)
	elif data_option == '6':
		low_vuln = get_low()
		bubble_chart(ips, low_vuln)
	elif data_option == '7':
		info_vuln == get_info_vulns()
		bubble_chart(ips, info_vuln)

def basic_scatter_chart(data_option):
	ips = get_ips()
	if data_option == '1':
		score = get_score()
		scatter_plot(ips, score)
	elif data_option == '2':
		total_vuln = get_total_vulnerabilities()
		scatter_plot(ips, total_vuln)
	elif data_option == '3':
		crits = get_crits()
		scatter_plot(ips, crits)
	elif data_option == '4':
		high_vuln = get_high()
		scatter_plot(ips, high_vuln)
	elif data_option == '5':
		medium_vuln = get_medium()
		scatter_plot(ips, medium_vuln)
	elif data_option == '6':
		low_vuln = get_low()
		scatter_plot(ips, low_vuln)
	elif data_option == '7':
		info_vuln == get_info_vulns()
		scatter_plot(ips, info_vuln)
	
def line_plot_chart(data_option):
	ips = get_ips()
	if data_option == '1':
		score = get_score()
		simple_line_plot(ips, score)
	elif data_option == '2':
		total_vuln = get_total_vulnerabilities()
		simple_line_plot(ips, total_vuln)
	elif data_option == '3':
		crits = get_crits()
		simple_line_plot(ips, crits)
	elif data_option == '4':
		high_vuln = get_high()
		simple_line_plot(ips, high_vuln)
	elif data_option == '5':
		medium_vuln = get_medium()
		simple_line_plot(ips, medium_vuln)
	elif data_option == '6':
		low_vuln = get_low()
		simple_line_plot(ips, low_vuln)
	elif data_option == '7':
		info_vuln == get_info_vulns()
		simple_line_plot(ips, info_vuln)
		
def stacked_bar():
	ips = get_ips()
	crits = get_crits()
	high = get_high()
	medium = get_medium()
	low = get_low()
	
	stacked_bar_chart(ips, crits, high, medium, low)
	
def area_chart():
	ips = get_ips()
	crits = get_crits()
	high = get_high()
	medium = get_medium()
	low = get_low()
	
	stacked_area_chart(ips, crits, high, medium, low)