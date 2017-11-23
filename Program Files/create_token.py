import getpass, os, re

def create_token(username, password, url, port):
	os.system("rm -rf token.txt")
	os.system("rm -rf report.txt")

	backslash = "\\"
	curl_cmd_1 = "curl -s -k -X POST -H 'Content-Type: application/json' -d \"{" + backslash + "\"username\\\":" + backslash + "\"" + username + backslash + "\"," + backslash + "\"password" + backslash + "\":" + backslash + "\"" + password + backslash + "\"}\" https://" + url + ":" + port + "/session/"


	os.system(curl_cmd_1 + " >> token.txt")

def get_token():
	token = open("token.txt", "r").readline()
	token = token[10:-2]
	return token
	