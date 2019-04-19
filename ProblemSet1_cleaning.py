import pandas as pd

df= pd.read_csv("parsed_results/boardgamegeek_dataset.csv", encoding= "latin-1")

df= df.replace("\n\t\t\t", "")
df= df.replace("\t\t", "")
df= df[['page_number', 'title', 'geek_rating', 'avg_rating', 'vote_number']]

df.to_csv("parsed_results/boardgamegeek_dataset.csv", index=False)
