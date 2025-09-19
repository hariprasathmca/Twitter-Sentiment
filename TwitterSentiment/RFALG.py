
#--------------------------------------------------------------
# Include Libraries
#--------------------------------------------------------------

import pandas as pd
from sklearn.model_selection import train_test_split
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn import metrics
from matplotlib import pyplot as plt
import numpy as np
import re
import csv
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score


	
def RForest(xtrain,ytrain,xtest,y_test):
	clf1 = RandomForestClassifier(max_depth=50, random_state=0,n_estimators=25)
	clf1.fit(xtrain,ytrain)
	y_pred = clf1.predict(xtest)

	mse=mean_squared_error(y_test, y_pred)
	mae=mean_absolute_error(y_test, y_pred)
	r2=r2_score(y_test, y_pred)
	
	
	print("---------------------------------------------------------")
	print("MSE VALUE FOR Random Forest IS %f "  % mse)
	print("MAE VALUE FOR Random Forest IS %f "  % mae)
	print("R-SQUARED VALUE FOR Random Forest IS %f "  % r2)
	rms = np.sqrt(mean_squared_error(y_test, y_pred))
	print("RMSE VALUE FOR Random Forest IS %f "  % rms)
	ac=accuracy_score(y_test,y_pred.round())
	print ("ACCURACY VALUE Random Forest IS %f" % ac)
	print("---------------------------------------------------------")
	

	result2=open("results/RFMetrics.csv", 'w')
	result2.write("Parameter,Value" + "\n")
	result2.write("MSE" + "," +str(mse) + "\n")
	result2.write("MAE" + "," +str(mae) + "\n")
	result2.write("R-SQUARED" + "," +str(r2) + "\n")
	result2.write("RMSE" + "," +str(rms) + "\n")
	result2.write("ACCURACY" + "," +str(ac) + "\n")
	result2.close()
	
	
	df =  pd.read_csv("results/RFMetrics.csv")
	acc = df["Value"]
	alc = df["Parameter"]
	colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
	explode = (0.1, 0, 0, 0, 0)  
	
	fig = plt.figure()
	plt.bar(alc, acc,color=colors)
	plt.xlabel('Parameter')
	plt.ylabel('Value')
	plt.title("Random Forest Metrics Value")
	fig.savefig("results/RFMetricsValue.png") 
	plt.pause(5)
	plt.show(block=False)
	plt.close()
 




def process(path):
	df = pd.read_csv(path,encoding='utf-8')
	print(df.head())
	y = df.label
	df.drop("label", axis=1)      #where numbering of news article is done that column is dropped in dataset
	X_train, X_test, y_train, y_test = train_test_split(df['text'], y, test_size=0.33, random_state=53)

	count_vectorizer = CountVectorizer(stop_words='english')
	count_train = count_vectorizer.fit_transform(X_train.values.astype('U'))                  # Learn the vocabulary dictionary and return term-document matrix.
	count_test = count_vectorizer.transform(X_test.values.astype('U'))
	
	RForest(count_train,y_train,count_test,y_test)

