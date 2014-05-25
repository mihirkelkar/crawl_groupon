#!/usr/bin/python
import mechanize
import re
def find():
	browser = mechanize.Browser()
	browser.addheaders = [('User-agent', "Mozilla/5.0")]
	browser.set_handle_robots(False)
	html = browser.open("http://www.groupon.com/local")
	html = ''.join([i if ord(i) < 128 else '' for i in html.read().lower()])
	match = re.findall('"open_state_info_link">([\w\s-]+)</a>', html)
	if match:
		fp = open("states", "w")
		for i in match:
			fp.write(i.title()+"\n")
		fp.close()	
	else:
		print "problem ?"


find()	
