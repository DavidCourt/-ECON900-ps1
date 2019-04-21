# -ECON900-ps1
Problem Set 1
This is a program to scrape page number, title, geek rating, average rating, and vote number from boardgamegeek.com then perform several forms of supervised learning.
This project contains four programs to run. 

1) run problemset1_request.py
This program requests the first 100 pages from the browse section of boardgame geek. 

Saves these files in a folder labeled html_files with the name boardgamegeek + the page number. 
You can change the range value to request a different number of pages. 

2) run problemset1_parse.py
This program uses beautiful soup to save data on page number, title, geek rating, average rating, and vote number to a pandas dataframe. 

Creates a dataframe
Reads the files you just requested. 
Uses Beautiful Soup to parse the data and get the page number, title, geek rating, average rating, and vote number for each boardgame from each page. 
Appends the dataframe you just created to include the data parsed.
Saves the pandas dataframe to a csv file in a folder labeled parsed_results with the name boardgamegeek_dataset.csv

3)Next run problemset1_cleaning.py
This program eliminates blank space and reorders the df columns. 

The data taken from the previous file has blank space. 
This file removes it so you only get the data you want.
Reorders the dataframe so you get the page number, title, geek_rating, average rating, and then vote number. 
This makes it much easier to use the data for machine learning. 
Saves the data in a csv file with the same name. 

4)Finally run problemset1_ml.py\
This program gives summary statistics, runs basic OLS, creates scatterplots of the page number to each variable, runs linear regression, knn regression, random forest regression, and random forest classification.

Gives info on the data contained in the dataset.
Gives summary statistics.
Runs simple OLS.
Creates 3 new columns in the dataframe called inv_geekrating, inv_avg_rating, inv_vote_num which are created by taking the reciprocal of each dependent variable.
Sepeartes the data into the explanatory variables (data) and dependent variable (target).
Seperate the data into two sets of variables: 
data consisting of the original variables (geek rating, average rating, and vote number)
data1 consisting of the new variables created (inv_geekrating, inv_avg_rating, and inv_vote_num).
Create 3 scatterplots: one for each of the original data variables to page number
Saves scatterplots in a folder named scatter_plots

Use test train split for data and data1 to create training and test data. 
Runs linear regression with data1 and creates a scatterplot of predictions to the true value. Also gives R^2 value.
Runs KNN regression with data creates a scatterplot of predictions to the true value. Also gives R^2 value.
Runs Random Forest regresion with data creates a scatterplot of predictions to the true value. Also gives R^2 value.
Runs Random Forest classification with data creates a scatterplot of predictions to the true value. 
Gives accuracy score, creates confusion matrix.
Finally gives feature importance for Random Forest regression and classification. 
 





