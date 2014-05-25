import mechanize
import re
from BeautifulSoup import BeautifulSoup
fp = open("final_cities", "r")
browser = mechanize.Browser()
browser.addheaders = [("User-agent", "Mozilla/5.0")]
browser.set_handle_robots(False)
city_list = [i.strip() for i in fp.readlines()]
for city in city_list:
	op = open(city, "w")
	html = browser.open("http://www.groupon.com/local/" + city)
	soup = BeautifulSoup(html)
	temp = soup.findAll("figure", {"class" : "featured-deal bhtracked"})
	temp_dealcards = soup.findAll("figure", {"class":"deal-card"})
	print "------------------- length of temp is " + str(len(temp)) + "------------------"
	for i in temp:
		try:
			op.write("*********************************\n")
			op.write(i.h2.a.text + "\n")
			op.write(i.h3.a.text + "\n")
			op.write(i.p.text + "\n")
			op.write("*********************************\n")
		except:
			continue
	print "------------------ length of temp2 is" + str(len(temp_dealcards)) + " ----------------------"
	for i in temp_dealcards:
		try:
			op.write("*********************************\n")
			link =  i.a.get("href")
			print link
			temphtml = browser.open("http://www.groupon.com" + link)
			souper = BeautifulSoup(temphtml)
			label = souper.findAll("h2", {"class" : "deal-page-title"})
			op.write(label[0].text + "\n")
			sublabel  = souper.findAll("h3", {"class" : "deal-subtitle"})
			op.write(sublabel[0].text + "\n")
			op.write("*********************************\n")
		except:
			continue
	"""if temp:
		for i in temp:
			print i
			op.write("---------------------\n")
			op.write(i.h2.a.text + "\n")
			op.write(i.h3.a.text + "\n")
			#op.write(i.p.text + "\n")
			op.write("---------------------\n")
	if temp_dealcards:
		for i in temp:
			print "THIS IS TEMP2"
			print i
			op.write("-----------------------\n")
			op.write(i.a.figcaption.p[0].text + "\n")
			op.write(i.a.figcaption.p[1].text + "\n")
			op.write(i.a.figcaption.p[2].text  + "\n")
			op.write(i.a.figcaption.p[3].text + "\n")
			op.write("------------------------------\n")
	"""	
	op.close()
	
