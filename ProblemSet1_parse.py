import os
from bs4 import BeautifulSoup
import glob
import pandas as pd

if not os.path.exists("parsed_results"):
	os.mkdir("parsed_results")

df = pd.DataFrame()

for one_file_name in glob.glob("html_files/*.html"):
	# print("parsing " + one_file_name)
	page_number = os.path.splitext(os.path.basename(one_file_name))[0].replace("boardgamegeekpage","")
	print(page_number)
	f= open(one_file_name, "r", encoding="utf-8")
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()
	game_table=soup.find("table", {"class": "collection_table"})
	game_row=game_table.find_all("tr", {"id": "row_"})
	for r in game_row:
		game_name=r.find("td", {"class": "collection_objectname"}).find("div", {"style": "z-index:1000;"}).find("a").text
		game_cell=r.find_all("td", {"class": "collection_bggrating"})
		game_geekrating = game_cell[0].text
		game_avgrating = game_cell[1].text
		game_votenum= game_cell[2].text
		df=df.append({
			'page_number': page_number,
			'title': game_name,
			'geek_rating': game_geekrating,
			'avg_rating': game_avgrating,
			'vote_number': game_votenum,
			}, ignore_index=True)

print(df)
df.to_csv("parsed_results/boardgamegeek_dataset.csv")


