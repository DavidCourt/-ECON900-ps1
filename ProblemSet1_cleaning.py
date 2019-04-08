import pandas as pd

df= pd.read_csv("parsed_results/boardgamegeek_dataset.csv", encoding= "latin-1")

df= df.replace("\n\t\t\t", "")
df= df.replace("\t\t", "")

df.to_csv("parsed_results/boardgamegeek_dataset.csv", index=False)
