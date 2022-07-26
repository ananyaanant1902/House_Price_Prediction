# -*- coding: utf-8 -*-
"""House-Price-Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ErAbu53JChWlZbxdtIAClOUjMvK5fbY_

**Importing the dependecies**
"""

import numpy as np #For making the data arrays'''
import pandas as pd #For analysis of data
import matplotlib.pyplot as pt #For plotting
import seaborn as sns #For plotting
import sklearn.datasets #For getting various datasets and algorithms
from sklearn.model_selection import train_test_split #for training and testing datasets
from xgboost import XGBRegressor # regression algorithm for price prediction
from sklearn import metrics #for evaluating the mode

"""**Importing dataset using sklearn**"""

house_price_dataset = sklearn.datasets.load_boston()
print(house_price_dataset)

"""More Structured form using **pandas**"""

#Loading the dataset to the pandas dataframe
house_price_dataframe=pd.DataFrame(house_price_dataset.data)
house_price_dataframe.head() #For first 5 values of the dataset
#No column names are showing, thus we will use the feature of the DataFrame function called columns

house_price_dataframe=pd.DataFrame(house_price_dataset.data,columns=house_price_dataset.feature_names) #since, feature names contains the columns name
house_price_dataframe.head()

"""Adding the target(price) column to the DataFrame"""

house_price_dataframe['Price']=house_price_dataset.target
house_price_dataframe.head()

"""Checking the no of rows and columns in the dataframe"""

house_price_dataframe.shape #returns the (rows and columns)(including price column)

"""Checking For Missing Values"""

house_price_dataframe.isnull().sum() #returns the sum of missing values in each column

"""*No need for processing, since no missing values*
Now Statistical Measures like mean, median, precentage, standard deviation...etc
"""

house_price_dataframe.describe() 
# standard deviation, mean...etc
# 25% of the given value of CRIM is less than 0.082045...etc
# 50% of the given value of CRIM is leaa than 0.256510....etc
# ...etc

"""Corelation between the data"""

correlation=house_price_dataframe.corr() #Will check the correlation between all the variables

"""Plotting Heat Map to understand the correlation"""

pt.figure(figsize=(12,12))
sns.heatmap(correlation, cbar=True, square= True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')

"""Splitting the data and the target(PRICE)"""

X = house_price_dataframe.drop(['Price'], axis=1) #removing the price and storing it in the X variable, we set axis=1 for removing columns; for removing row axis=0
Y = house_price_dataframe['Price'] #storing the column of price in the Y
print(X)
print(Y)

"""Splitting the data into train and test data"""

X_train, X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""Model Training
Using XGBOOST Regressor Model
"""

model=XGBRegressor()
#training the model with xgb
model.fit(X_train, Y_train)

"""Evaluation"""

#prediction on training data
train_data_prediction=model.predict(X_train)
print(train_data_prediction)

#R squared error
score_1=metrics.r2_score(Y_train,train_data_prediction)

#Absolute mean error
score_2=metrics.mean_absolute_error(Y_train,train_data_prediction)

print("R squared error value is :", score_1)

print("Absolute mean error value is :", score_2)

"""Now we will do the prediction for our Testing data"""

#prediction on testing data
test_data_prediction=model.predict(X_test)
print(test_data_prediction)

#R squared error
score_1=metrics.r2_score(Y_test,test_data_prediction)

#Absolute mean error
score_2=metrics.mean_absolute_error(Y_test,test_data_prediction)

print("R squared error value for Testing data is :", score_1)

print("Absolute mean error value for Testing data is :", score_2)

"""Scatter plot between actual price and predicted price"""

pt.scatter(Y_train, train_data_prediction)
pt.xlabel("Actual Price")
pt.ylabel("Predicted Price")
pt.show()

#for test
pt.scatter(Y_test, test_data_prediction)
pt.xlabel("Actual Price")
pt.ylabel("Predicted Price")
pt.show()

"""We used XGBRegressor boost model because the data set is less
Also, the results were **fine**
"""