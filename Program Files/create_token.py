"""
Name: create_token.py
Author: Wesley Lee
Assignment: Visualization Project
Date Created: 11-02-2017
Last Updated: 11-23-2017

Description:
	Creates a new token and gets the token from the file.
"""

import getpass, os, re

# Creates a token for the Nessus server
def create_token(username, password, url, port):
	os.system("rm -rf token.txt")
	os.system("rm -rf report.txt")

	backslash = "\\"
	curl_cmd_1 = "curl -s -k -X POST -H 'Content-Type: application/json' -d \"{" + backslash + "\"username\\\":" + backslash + "\"" + username + backslash + "\"," + backslash + "\"password" + backslash + "\":" + backslash + "\"" + password + backslash + "\"}\" https://" + url + ":" + port + "/session/"


	os.system(curl_cmd_1 + " >> token.txt")

# Gets a token from the token file
def get_token():
	token = open("token.txt", "r").readline()
	token = token[10:-2]
	return token
	