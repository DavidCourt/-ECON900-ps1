import urllib.request
import ssl
import os
import time

if not os.path.exists("html_files"):
	os.mkdir("html_files")
unverified_context= ssl._create_unverified_context()

for i in range(1061):
	print("page " + str(i+1))
	f= open("html_files/boardgamegeekpage" + str(i+1) + ".html", "wb")
	response=urllib.request.urlopen('https://boardgamegeek.com/browse/boardgame/page/' + str(i+1))
	html=response.read()
	f.write(html)
	f.close()
	time.sleep(60)



















# import urllib.request
# import ssl
# import os
# import time
# import datetime

# if not os.path.exists("html_files"):
# 	os.mkdir("html_files")
# unverified_context= ssl._create_unverified_context()

# for i in range(2):
# 	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%m%d%H%M')
# 	print(str(i) + ": " + current_time_stamp)
# 	f=open("html_files/kayak" + current_time_stamp + ".html", "wb")
# 	responseK=urllib.request.urlopen('https://www.kayak.com/flights/IAH-WAS/2019-08-16/2adults?sort=price_a')
# 	g=open("html_files/expedia" + current_time_stamp + ".html", "wb")
# 	responseE=urllib.request.urlopen('https://www.expedia.com/Flights-Search?flight-type=on&starDate=08%2F16%2F2019&mode=search&trip=oneway&leg1=from%3AHouston%2C+TX+%28IAH-George+Bush+Intercontinental%29%2Cto%3AWashington%2Cdeparture%3A08%2F16%2F2019TANYT&passengers=children%3A0%2Cadults%3A2%2Cseniors%3A0%2Cinfantinlap%3AY&fareCalendarPrice=109')
# 	h=open("html_files/travelocity" + current_time_stamp + ".html", "wb")
# 	responseT=urllib.request.urlopen('https://www.travelocity.com/Flights-Search?flight-type=on&starDate=08%2F16%2F2019&_xpid=11905%7C1&mode=search&trip=oneway&leg1=from%3AHouston%2C+TX+%28IAH-George+Bush+Intercontinental%29%2Cto%3AWashington%2C+DC+%28WAS-All+Airports%29%2Cdeparture%3A08%2F16%2F2019TANYT&passengers=children%3A0%2Cadults%3A2%2Cseniors%3A0%2Cinfantinlap%3AY')
# 	htmlK= responseK.read()
# 	f.write(htmlK)
# 	f.close()
# 	htmlE=responseE.read()
# 	g.write(htmlE)
# 	g.close()
# 	htmlT= responseT.read()
# 	h.write(htmlT)
# 	h.close()
# 	time.sleep(86400)