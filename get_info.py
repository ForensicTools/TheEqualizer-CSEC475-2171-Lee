"""
Name: get_info.py
Author: Wesley Lee
Assignment: Visualization Project
Date: 11-02-2017
"""

#!/usr/bin/python
import os

def get_info(token, port):
	curl_cmd = "curl -s -k -X GET -H \"X-Cookie: token=" + token + "\" https://localhost:" + port + "/scans/ | python -m json.tool"
	os.system(curl_cmd)
	
def get_report(token, port, report_id, option):
	os.system("rm -rf report.txt")
	curl_cmd = "curl -s -k -X GET -H \"X-Cookie: token=" + token + "\" https://localhost:" + port + "/scans/" + report_id + "/ | python -m json.tool"
	if option == '2':
		os.system(curl_cmd + " >> report.txt")
		os.system(curl_cmd)
	elif option >= '3':
		os.system(curl_cmd + " >> report.txt")

def get_num_of_hosts():
	hosts = []
	with open("report.txt") as f:
		for line in f:
			if "\"num_hosts\"" in line:
				hosts.append(line[21:-2])
				
	return hosts

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

def get_crits():
	crits = []
	with open("report.txt") as f:
		for line in f:
			if "\"critical\"" in line:
				crits.append(line[24:-2])
	return crits	
	
def get_high():
	high = []
	with open("report.txt") as f:
		for line in f:
			if "\"high\"" in line:
				high.append(line[20:-2])
	return high
	
def get_medium():
	medium = []
	with open("report.txt") as f:
		for line in f:
			if "\"medium\"" in line:
				medium.append(line[22:-2])
	return medium

def get_low():
	low = []
	with open("report.txt") as f:
		for line in f:
			if "\"low\"" in line:
				low.append(line[19:-2])
	return low

def get_score():
	score = []
	with open("report.txt") as f:
		for line in f:
			if "\"score\"" in line:
				score.append(line[21:-2])
	return score
	
def get_info_vulns():
	info = []
	with open("report.txt") as f:
		for line in f:
			if "\"info\"" in line:
				info.append(line[20:-2])
	return info