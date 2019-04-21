import urllib.request
import ssl
import os
import time

if not os.path.exists("html_files"):
	os.mkdir("html_files")
unverified_context= ssl._create_unverified_context()

for i in range(100):
	print("page " + str(i+1))
	f= open("html_files/boardgamegeekpage" + str(i+1) + ".html", "wb")
	response=urllib.request.urlopen('https://boardgamegeek.com/browse/boardgame/page/' + str(i+1))
	html=response.read()
	f.write(html)
	f.close()
	time.sleep(30)
