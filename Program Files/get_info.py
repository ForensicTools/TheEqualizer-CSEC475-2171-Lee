"""
Name: get_info.py
Author: Wesley Lee
Assignment: Visualization Project
Date Created: 11-02-2017
Last Updated: 11-23-2017

Description:
	Gets Info from both the Nessus Server and scans and either uses the 
	data for other functions or displays them.
"""

#!/usr/bin/python
import os, getpass

# Asks for the username for the Nessus Server
def get_username():
	os.system("clear")
	print("Enter information for Nessus Server:")
	username = raw_input("\nUsername: ")
	return username

# Asks for the password for the Nessus Server
def get_password():
	password = getpass.getpass()
	return password

# Asks for the url of the Nessus Server
def get_url():
	url = raw_input("IP Address or URL of Nessus Server [Default = 127.0.0.1]: ")
	return url

# Asks for the port number of the Nessus Server
def get_port():
	port = raw_input("Port the server is running on [Default = 8834]: ")
	return port

# Gets information and displays information about the Nessus Server
def get_info(token, url, port, option):
	curl_cmd = "curl -s -k -X GET -H \"X-Cookie: token=" + token + "\" https://" + url + ":" + port + "/scans/ | python -m json.tool"
	
	os.system(curl_cmd)

# Gets a report of a specific scan
def get_report(token, url, port, report_id, option):
	os.system("rm -rf report.txt")
	curl_cmd = "curl -s -k -X GET -H \"X-Cookie: token=" + token + "\" https://" + url + ":" + port + "/scans/" + report_id + "/ | python -m json.tool"
		
	if option == '2':
		os.system(curl_cmd + " >> report.txt")
		os.system(curl_cmd)
	elif option >= '3':
		os.system(curl_cmd + " >> report.txt")

# Gets the Number of hosts from the scan
def get_num_of_hosts():
	hosts = []
	with open("report.txt") as f:
		for line in f:
			if "\"num_hosts\"" in line:
				hosts.append(line[21:-2])
				
	return hosts

# Gets the ips from the scan	
def get_ips():
	ips = []
	with open("report.txt") as f:
		for line in f:
			if "\"hostname\"" in line:
				if line[25:-3] == "name":
					None
				else:
					ips.append(line[25:-3])
	return ips

# Gets the number of critical vulnerabilities per IP
def get_crits():
	crits = []
	with open("report.txt") as f:
		for line in f:
			if "\"critical\"" in line:
				crits.append(line[24:-2])
	return crits	

# Gets the number of high vulnerabilities per IP	
def get_high():
	high = []
	with open("report.txt") as f:
		for line in f:
			if "\"high\"" in line:
				high.append(line[20:-2])
	return high

# Gets the number of medium vulnerabilities per IP
def get_medium():
	medium = []
	with open("report.txt") as f:
		for line in f:
			if "\"medium\"" in line:
				medium.append(line[22:-2])
	return medium

# Gets the number of low vulnerabilities per IP
def get_low():
	low = []
	with open("report.txt") as f:
		for line in f:
			if "\"low\"" in line:
				low.append(line[19:-2])
	return low

# Gets the number of Info vulnerabilities per IP
def get_info_vulns():
	info = []
	with open("report.txt") as f:
		for line in f:
			if "\"info\"" in line:
				info.append(line[20:-2])
	return info

# Gets the the score of each IP
def get_score():
	score = []
	with open("report.txt") as f:
		for line in f:
			if "\"score\"" in line:
				score.append(line[21:-2])
	return score	

# Gets the number of total vulnerabilities per IP	
def get_total_vulnerabilities():
	ips = get_ips()
	crits = get_crits()
	high = get_high()
	medium = get_medium()
	low = get_low()
	total_vulns = []
	vulns_list = []
	i = 0
	x = 0
	y = 0
	t = 0
	tmp = 0

	while x < len(ips):
		vulns_list.append(crits[x])
		vulns_list.append(high[x])
		vulns_list.append(medium[x])
		vulns_list.append(low[x])
		x += 1
	
	y = 0
	while t < len(ips):
		while y < (len(ips)):
			tmp = 0
			tmp += int(vulns_list[0]) + int(vulns_list[1]) + int(vulns_list[2]) + int(vulns_list[3])
	
			total_vulns.append(tmp)
			del vulns_list[0:4]
			
			y += 1
			
		t += 1	

	return total_vulns