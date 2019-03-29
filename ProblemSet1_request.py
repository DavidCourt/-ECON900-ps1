import urllib.request
import ssl
import os
import time
import datetime

if not os.path.exists("html_files"):
	os.mkdir("html_files")
unverified_context= ssl._create_unverified_context()

for i in range(1):
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%d%H')
	print(str(i) + ": " + current_time_stamp)
	f= open("html_files/kayak" + current_time_stamp + ".html", "wb")
	response=urllib.request.urlopen('https://www.kayak.com/flights/IAH-WAS/2019-08-16/2019-08-16?sort=price_a')
	print(response)
	html= response.read()
	f.write(html)
	f.close()
	time.sleep(60)