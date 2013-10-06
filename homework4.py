#!/usr/local/bin/python
import csv

from sklearn.datasets import load_files, datasets, linear_model
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB




#---------HOMEWORK ASSIGNMENT------------------------------
#1) Split the data into train and test. You will use one as your training set and the other for validation. 
#Feel free to make multiple splits or use cross validation to make multiple splits

# Load the text data
train_data = csv.reader(open("train.csv","rb"))

test_data = csv.reader(open("test.csv","rb"))

#2) Build a logistic regression model to predict whether the comment is an insult. Explore regularization again and how it effects your model.

#You can use R - ( glm(...., family='binomial'), glmnet(..., family='binomial') ) or Python (sklearn.linear_model.LogisticRegression)


#Get the Comments

#Get the Insults

from sklearn.datasets.samples_generator import make_regression


# Create linear regression object
regr = sklearn.linear_model.LogisticRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

#Use AUC score to evaluate your model.




#3) Build a Naive Bayes model on the same task. Compare the performance with the logistic regression model

#Use sklearn.naive_bayes.MultinomialNB

#Try out different prior values and see how this effects performance.

#Use AUC score to evaluate your model. Please submit the code and output using Schoology.