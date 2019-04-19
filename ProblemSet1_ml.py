import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from sklearn import linear_model
from sklearn.neighbors import KNeighborsRegressor

from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

boardgame= pd.read_csv("parsed_results/boardgamegeek_dataset.csv", encoding= "latin-1")
ols = smf.ols('page_number ~ geek_rating + avg_rating + vote_number', data=boardgame).fit()
#print(ols.summary())

data= boardgame.iloc[:,2:5]
#print(data.head())
target= boardgame.iloc[:,0]
#print(target.head())
data= data.values
target= target.values

plt.scatter(target, data[:,0])
plt.title("Geek Rating")
plt.xlabel("Page Number")
plt.ylabel("Geek Ranking")
plt.savefig("Geek_Rank.png")
plt.clf()
plt.scatter(target, data[:,1])
plt.title("Average Rating")
plt.xlabel("Page Number")
plt.ylabel("Average Rating")
plt.savefig("Avg_Rating.png")
plt.clf()
plt.scatter(target, data[:,2])
plt.title("Vote Number")
plt.xlabel("Page Number")
plt.ylabel("Number of Votes")
plt.savefig("Vote_Number.png")
plt.clf()


data_training, data_test, target_training, target_test= train_test_split(data, target, test_size=.25, random_state=0)
linear_machine= linear_model.LinearRegression()
linear_machine.fit(data_training,target_training)
prediction= linear_machine.predict(data_test)
plt.scatter(target_test, prediction)
plt.title("Linear Prediction")
plt.xlabel('Target Test')
plt.ylabel('Prediction')
plt.savefig("scatter_linear_prediction.png")
print(metrics.r2_score(target_test, prediction))

Knn_Regression_Machine= KNeighborsRegressor(n_neighbors=1)
Knn_Regression_Machine.fit(data_training,target_training)
prediction1= Knn_Regression_Machine.predict(data_test)
plt.scatter(target_test, prediction1)
plt.title("KNN Prediction")
plt.xlabel('Target Test')
plt.ylabel('Prediction')
plt.savefig("scatter_knn_regression_prediction.png")
plt.clf()
print(metrics.r2_score(target_test, prediction1))

