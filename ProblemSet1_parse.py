import os
from bs4 import BeautifulSoup
import glob
import pandas as pd

if not os.path.exists("parsed_results"):
	os.mkdir("parsed_results")

df = pd.DataFrame()

for one_file_name in glob.glob("html_files/*.html"):
	print("parsing " + one_file_name)
	scrapping_time = os.path.splitext(os.path.basename(one_file_name))[0].replace("coinmarketcap","")
	print(scrapping_time)
	f= open(one_file_name, "r", encoding="utf-8")
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()
	game_table=soup.find("table", {"id": "collectionitems"})
	game_tbody=game_table.find("tbody")
	game_row=game_tbody.find_all("tr")
	for r in game_row:
		game_title=r.find("td", {"id": "CEcell_objectname1"}).find("div", {"id": "results_objectname1"}).find("a").text
		game_geekrating=r.find("td", {"class": "collection_bggrating"}).text
		game_avgrating=r.find("td", {"class": "collection_bggrating"}).text
		game_votenum=r.find("td", {"class": "collection_bggrating"}).text
		game_price=r.find("td", {"class": "collection_shop"}).find("div", {"class": "aad"}).find("div").find("div").text


