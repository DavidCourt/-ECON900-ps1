import os
from bs4 import BeautifulSoup
import glob
import pandas as pd

if not os.path.exists("parsed_results"):
	os.mkdir("parsed_results")

df = pd.DataFrame()

for one_file_name in glob.glob("html_files/*.html"):
	print("parsing " + one_file_name)
	scrapping_time = os.path.splitext(os.path.basename(one_file_name))[0].replace("boardgamegeek","")
	print(scrapping_time)
	f= open(one_file_name, "r", encoding="utf-8")
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()
	game_table=soup.find("table", {"class": "collection_table"})
	game_row=game_table.find_all("tr", {"id": "row_"})
	for r in game_row:
		game_title=r.find("td", {"id": "CEcell_objectname1"}).find("div", {"id": "results_objectname1"}).find("a").text
		print(game_title)
		game_cell=r.find_all("td", {"class": "collection_bggrating"})
		i=0
		for c in game_cell:
			if i == 0:
				game_geekrating=c.text
			elif i == 1:
				game_avgrating=c.text
			elif i == 2:
				game_votenum=c.text

			i=i+1	
		print("rating" + game_geekrating)
		print("avg" + game_avgrating)
		print("vote" + game_votenum)
		game_price=r.find("td", {"class": "collection_shop"}).find("div", {"class": "aad"}).text
		print(game_price)

		df=df.append({
			'scrapping_time': scrapping_time,
			'title': game_title,
			'geek_rating': game_geekrating,
			'avg_rating': game_avgrating,
			'vote_number': game_votenum,
			'list_price': game_price
			}, ignore_index=True)

print(df)


