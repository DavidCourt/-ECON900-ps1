import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
import numpy as np
from sklearn import metrics

boardgame= pd.read_csv("parsed_results/boardgamegeek_dataset.csv", encoding= "latin-1")
#print(boardgame.head())

# #going to be doing classification
data= boardgame.iloc[:,1:4]
# print(data.head())
target= boardgame.iloc[:,0]
#print(target.head())
data= data.values
target= target.values

# plt.scatter(target, data[:,1])
# plt.savefig("scatter1.png")

# knn2 = KNeighborsClassifier()
# param_grid= {'n_neighbors' : np.arange(1,100)}
# knn_gscv = GridSearchCV(knn2, param_grid, cv=10).fit(data, target)
# print(knn_gscv.best_params_)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(data, target)

data_training, data_test, target_training, target_test= train_test_split(data, target, test_size=.2, random_state=0, stratify=target)
kfold_machine= KFold(n_splits=5)
kfold_machine.get_n_splits(data)
#print(kfold_machine)

# knn_cv = KNeighborsClassifier(n_neighbors=1)
# cv_scores = cross_val_score(knn_cv, data, target, cv=5)
# print(cv_scores)
# print("cv_scores mean:{}".format(np.mean(cv_scores)))


X=[
	[7.34,6,200],
	[7.5,6.5,300],
	[6,6.4, 1000],
	[6.63, 6.63, 600],
	]

results=knn.predict(X)
print(results)
