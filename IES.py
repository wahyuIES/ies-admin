#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("web.txt","r");
	link = raw_input("nama website \n(contoh www.site.com): ")
	print "\n\nlink salah : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK >> ",req_link
 
def Credit():
 print "##########################"
 print "#  *** admin finder ***  #"
 print "#  * author:MR.W4HYU *  #"
 print "# *indonesian error system * #"
 print "#  thanks all member             #"
 print "##########################"
                          

Credit()
findAdmin()