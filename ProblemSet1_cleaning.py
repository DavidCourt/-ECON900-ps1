import pandas as pd

df= pd.read_csv("parsed_results/boardgamegeek_dataset.csv", encoding= "latin-1")

df= df.replace("\n\t\t\t", "")
df= df.replace("\t\t", "")
df= df[['page_number', 'avg_rating', 'geek_rating', 'vote_number', 'title']]

df.to_csv("parsed_results/boardgamegeek_dataset.csv", index=False)
