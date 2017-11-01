#!/usr/bin/python

import os

def get_info(token, port):
	curl_cmd = "curl -s -k -X GET -H \"X-Cookie: token=" + token + "\" https://localhost:" + port + "/scans/ | python -m json.tool"
	
	os.system(curl_cmd)
	
	
def get_report(token, port, report_id):
	os.system("rm -rf report.txt")
	curl_cmd = "curl -s -k -X GET -H \"X-Cookie: token=" + token + "\" https://localhost:" + port + "/scans/" + report_id + "/ | python -m json.tool"
	os.system(curl_cmd + " >> report.txt")
	os.system(curl_cmd)
