import os
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

from sklearn import linear_model
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier

from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

if not os.path.exists("scatter_plots"):
	os.mkdir("scatter_plots")

boardgame= pd.read_csv("parsed_results/boardgamegeek_dataset.csv", encoding= "latin-1")
print(boardgame.info())
print('\n')
print(boardgame.describe())
print('\n')
print("Missing Values: " + str(boardgame.isnull().values.any()))
print('\n')

ols = smf.ols('page_number ~ geek_rating + avg_rating + vote_number', data=boardgame).fit()
print(ols.summary())
print('\n')
data= boardgame.iloc[:,2:5]
data["inv_geekrating"]= 1/data["geek_rating"]
data["inv_avg_rating"]=1/data["avg_rating"]
data["inv_vote_num"]= 1/data["vote_number"]
data1= data.iloc[:,3:6]
data=data.iloc[:,0:3]
target= boardgame.iloc[:,0]
target= target.values

plt.scatter(data.values[:,0], target)
plt.title("Geek Rating")
plt.xlabel("Geek Rating")
plt.ylabel("Page Number")
plt.savefig("scatter_plots/Geek_Rank.png")
plt.clf()

plt.scatter(data.values[:,1], target)
plt.title("Average Rating")
plt.xlabel("Average Rating")
plt.ylabel("Page Number")
plt.savefig("scatter_plots/Avg_Rating.png")
plt.clf()

plt.scatter(data.values[:,2], target)
plt.title("Vote Number")
plt.xlabel("Number of Votes")
plt.ylabel("Page Number")
plt.savefig("scatter_plots/Vote_Number.png")
plt.clf()

data1_training, data1_test, target_training, target_test= train_test_split(data1, target, test_size=.2, random_state=0)
linear_machine= linear_model.LinearRegression()
linear_machine.fit(data1_training,target_training)
prediction= linear_machine.predict(data1_test)
plt.scatter(target_test, prediction)
plt.title("Linear Prediction")
plt.xlabel('Target Test')
plt.ylabel('Prediction')
plt.savefig("scatter_plots/scatter_linear_prediction.png")
plt.clf()
linear_r2=metrics.r2_score(target_test, prediction)
print("Linear R^2: " + str(linear_r2))

# knn= KNeighborsClassifier()
# param_grid= {'n_neighbors' : np.arange(1,100)}
# knn_gscv = GridSearchCV(knn, param_grid, cv=10).fit(data, target)
# print(knn_gscv.best_params_)

data_training, data_test, target_training, target_test= train_test_split(data, target, test_size=.2, random_state=0)
Knn_Regression_Machine= KNeighborsRegressor(n_neighbors=1)
Knn_Regression_Machine.fit(data_training,target_training)
prediction1= Knn_Regression_Machine.predict(data_test)
plt.scatter(target_test, prediction1)
plt.title("KNN Prediction")
plt.xlabel('Target Test')
plt.ylabel('Prediction')
plt.savefig("scatter_plots/scatter_knn_regression_prediction.png")
plt.clf()
KNN_R2=metrics.r2_score(target_test, prediction1)
print("KNN R^2: "+ str(KNN_R2))

random_forest_regressor= RandomForestRegressor(n_estimators=101)
random_forest_regressor.fit(data_training, target_training)
prediction2= random_forest_regressor.predict(data_test)
plt.scatter(target_test, prediction2)
plt.title("Random Forest Regression Prediction")
plt.xlabel('Target Test')
plt.ylabel('Prediction')
plt.savefig("scatter_plots/scatter_random_forest_regression_prediction.png")
plt.clf()
Random_Forest_R2= metrics.r2_score(target_test, prediction2)
print("Random Forest R^2: "+ str(Random_Forest_R2))

random_forest_classifier= RandomForestClassifier(n_estimators=101)
random_forest_classifier.fit(data_training, target_training)
prediction3= random_forest_classifier.predict(data_test)
plt.scatter(target_test, prediction3)
plt.title("Random Forest Classifier Prediction")
plt.xlabel('Target Test')
plt.ylabel('Prediction')
plt.savefig("scatter_plots/scatter_random_forest_classifier_prediction.png")
plt.clf()
Random_Forest_accuracy=accuracy_score(target_test, prediction3)
print("Random Forest Accuracy Score: "+ str(Random_Forest_accuracy))
print('\n')

confusion_matrix= pd.DataFrame(confusion_matrix(target_test, prediction3),columns=['Predict O', "Predict 1", "Predict 2", "Predict 3", "Predict 4", "Predict 5", "Predict 6", "Predict 7", "Predict 8", "Predict 9", "Predict 10"
, "Predict 11", "Predict 12", "Predict 13", "Predict 14", "Predict 15", "Predict 16", "Predict 17", "Predict 18", "Predict 19", "Predict 20"
, "Predict 21", "Predict 22", "Predict 23", "Predict 24", "Predict 25", "Predict 26", "Predict 27", "Predict 28", "Predict 29", "Predict 30"
, "Predict 31", "Predict 32", "Predict 33", "Predict 34", "Predict 35", "Predict 36", "Predict 37", "Predict 38", "Predict 39", "Predict 40"
, "Predict 41", "Predict 42", "Predict 43", "Predict 44", "Predict 45", "Predict 46", "Predict 47", "Predict 48", "Predict 49", "Predict 50"
, "Predict 51", "Predict 52", "Predict 53", "Predict 54", "Predict 55", "Predict 56", "Predict 57", "Predict 58", "Predict 59", "Predict 60"
, "Predict 61", "Predict 62", "Predict 63", "Predict 64", "Predict 65", "Predict 66", "Predict 67", "Predict 68", "Predict 69", "Predict 70"
, "Predict 71", "Predict 72", "Predict 73", "Predict 74", "Predict 75", "Predict 76", "Predict 77", "Predict 78", "Predict 79", "Predict 80"
, "Predict 81", "Predict 82", "Predict 83", "Predict 84", "Predict 85", "Predict 86", "Predict 87", "Predict 88", "Predict 89", "Predict 90"
, "Predict 91", "Predict 92", "Predict 93", "Predict 94", "Predict 95", "Predict 96", "Predict 97", "Predict 98", "Predict 99"],index= ['True O', "True 1", "True 2", "True 3", "True 4", "True 5", "True 6", "True 7", "True 8", "True 9", "True 10"
, "True 11", "True 12", "True 13", "True 14", "True 15", "True 16", "True 17", "True 18", "True 19", "True 20"
, "True 21", "True 22", "True 23", "True 24", "True 25", "True 26", "True 27", "True 28", "True 29", "True 30"
, "True 31", "True 32", "True 33", "True 34", "True 35", "True 36", "True 37", "True 38", "True 39", "True 40"
, "True 41", "True 42", "True 43", "True 44", "True 45", "True 46", "True 47", "True 48", "True 49", "True 50"
, "True 51", "True 52", "True 53", "True 54", "True 55", "True 56", "True 57", "True 58", "True 59", "True 60"
, "True 61", "True 62", "True 63", "True 64", "True 65", "True 66", "True 67", "True 68", "True 69", "True 70"
, "True 71", "True 72", "True 73", "True 74", "True 75", "True 76", "True 77", "True 78", "True 79", "True 80"
, "True 81", "True 82", "True 83", "True 84", "True 85", "True 86", "True 87", "True 88", "True 89", "True 90"
, "True 91", "True 92", "True 93", "True 94", "True 95", "True 96", "True 97", "True 98", "True 99"])
print(confusion_matrix)
confusion_matrix.to_csv("confusion_matrix.csv")
print('\n')

print(dict(zip(data.columns, random_forest_regressor.feature_importances_)))
print(dict(zip(data.columns, random_forest_classifier.feature_importances_)))
