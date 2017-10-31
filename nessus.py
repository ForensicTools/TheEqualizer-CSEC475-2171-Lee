"""
Name: ###FILENAME###
Author: Wesley Lee
Assignment: ###Assignment Name###
Date: ###Current Date###
"""
import pynessus

with Nessus('127.0.0.1:8834') as nes:
	nes.Login('wlee', 'Superman7562@#$')
	logging.info('Feeds: %s', nes.Feed())