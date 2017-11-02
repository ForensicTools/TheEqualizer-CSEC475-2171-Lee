from get_info import get_info, get_report, get_num_of_hosts, get_ips, get_crits, get_high, get_medium, get_low, get_score
from graphs import pie_chart, bar_chart, bubble_chart, scatter_plot, simple_line_plot

def print_stuff():
	hosts = get_num_of_hosts()
	ips = get_ips()
	crits = get_crits()
	high = get_high()
	medium = get_medium()
	low = get_medium()
	score = get_score()
	
	
	print hosts
	print ips
	print crits
	print high
	print medium
	print low
	print score

def basic_pie_chart():
	ips = get_ips()
	score = get_score()
	pie_chart(ips, score)
	
def basic_bar_chart():
	ips = get_ips()
	score = get_score()
	bar_chart(ips, score)
	
def basic_bubble_chart():
	ips = get_ips()
	score = get_score()
	bubble_chart(ips, score)

def basic_scatter_chart():
	ips = get_ips()
	score = get_score()
	scatter_plot(ips, score)
	
def line_plot_chart():
	ips = get_ips()
	score = get_score()
	simple_line_plot(ips, score)