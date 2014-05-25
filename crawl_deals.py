import mechanize
import re
fp = open("states", 'r')
states_list = [i.strip().lower().replace(" ", "-") for i in fp.readlines()]
states_list_set = set(states_list)
#print states_list
op = open("final_cities", "w")
browser = mechanize.Browser()
browser.addheaders = [('User-agent', 'Mozilla/5.0')]
browser.set_handle_robots(False)
cities = []
for i in states_list:
	html = browser.open("http://www.groupon.com/local/" + i)
	html = "".join([i if ord(i) < 128 else "" for i in html.read().lower()])
	match = re.findall('local/([\w\-\s]+)"', html)
	if match:
		cities += match
	else:
		print "problem ?"
cities_set = set(cities)
cities = [i for i in list(cities_set - states_list_set) if i not in ["restaurants", "nightlife", "hair-salons"]]
	
op.write("\n".join(cities))
op.close()

		
