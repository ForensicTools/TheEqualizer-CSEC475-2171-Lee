"""
Name: ###FILENAME###
Author: Wesley Lee
Assignment: ###Assignment Name###
Date: ###Current Date###
"""
import string
from lists import *
from looper import *

def ipgetter(iplist):
	a = set(iplist)
	ips = []
	ips += a
	return ips
	
def vuln_to_list(ips):
	for i in range(len(ips)):
		with open('test_input.txt', 'r') as searchfile:
			for line in searchfile:
				if ips[i] in line:
					ip1 += line				
	return(ip1)
	
def main():
	with open("test_input.txt","r") as f:
		iplist = [r.split()[0] for r in f]
	
	ips = ipgetter(iplist)
	vuln_to_list(ips)
	
if __name__ == "__main__":
	main()