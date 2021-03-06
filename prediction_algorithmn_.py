# -*- coding: utf-8 -*-
"""Prediction Algorithmn .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YaZ_BZwHfLDCH7IaZdLrMJdjBdcOCqi4
"""

#This program is the first orginal solo work of Mohamed Yousuf 

import pandas as pd
import csv
import random as rnd
import random
import os
import numpy as np
from numpy import mean
from numpy import std
from matplotlib import pyplot
import seaborn as sns
from IPython.display import Image
from sklearn.preprocessing import MultiLabelBinarizer
!pip install scikit-multilearn
from skmultilearn.problem_transform import BinaryRelevance
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from skmultilearn.model_selection import iterative_train_test_split
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegression
import sklearn.metrics as metrics
from skmultilearn.problem_transform import LabelPowerset
from sklearn.ensemble import RandomForestClassifier
import time
from sklearn.model_selection import GridSearchCV
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.metrics import precision_score
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score
from skmultilearn.model_selection import IterativeStratification
from skmultilearn.model_selection import iterative_train_test_split
from sklearn.neural_network import MLPClassifier

dataf = pd.read_csv("datasetupdatedsep4.csv")
# x=dataf.iloc[0:100,1:52]
# print(dataf.iloc[0:40,52])

# dataf["DER-1"]=np.where(dataf["DER-1"]=="T",1,0)
dataf["PTSD-2"]=np.where(dataf["PTSD-2"]=="T",1,0)
# dataf.drop(['HYPOCHRON','DER-1','APPEAR FEAR','NEURO','MUSCLE'],axis=1)
# print(dataf["DER-1"],dataf["PTSD-2"])
# print(dataf["DER-1"])
print(dataf)
# print(dataf["SNORING"])

#Assigning Labels
dataf["ADHD"]=np.where(dataf["ATTN"]>=2,1,0)
dataf["Depression"]=np.where(dataf["DEPR-1"]>=2,1,0)
# dataf["Delirium"]=np.where(dataf["DER-1"]=="1",1,0)
# print(dataf["Delirium"])
dataf["Dementia"]=np.where(dataf["DEMEN-1"]>=1,1,0)


# print(dataf["SUBSTANS-1"],dataf["SUBSTANS-2"],dataf["SUBSTANS-3"])
#Substance-Abuse:
#Any one of the symptoms of substance abuse needs to be satisfied with a score of greater than 1
dataf["SUBSTANCE-ABUSE"]=np.where(((dataf["SUBSTANS-1"]>=1) | (dataf["SUBSTANS-2"]>=1)) | (dataf["SUBSTANS-3"]>=1),1,0)

#Schizophrenia: Any one of the symptoms of Schizophrenia needs to be satisfied with a score of greater than 1
dataf["Schizophrenia"]=np.where(((dataf["SCHIZO-1"]>=1) | (dataf["SCHIZO-2"]>=1)),1,0)

#Bipolar Disorder
#The conditional statement is that either( BIPOLAR-1 or (BIPOLAR-1 and DEPR-1) ) need to be satisfied for this diease to be
#labeled
# dataf["BIPOLAR DISORDER SAMPLE COLUMN"] = np.where((dataf["BIPOLAR-1"]>=2) & (dataf["DEPR-1"]>=2),1,0)
dataf["Bipolar Disorder"]=np.where(((dataf["BIPOLAR-1"]>=2) | ((dataf["BIPOLAR-1"]>=2) & (dataf["DEPR-1"]>=2))),1,0)
# print(dataf)
# dataf.drop(["BIPOLAR DISORDER SAMPLE COLUMN"],axis=1)
# print(dataf["BIPOLAR DISORDER SAMPLE COLUMN"])

#Panic Disorder
#only one feature,"PA" needs to be satisfied for panic disorder to exist
dataf["PANIC DISORDER"]= np.where(dataf["PA"]>=2,1,0)

#Specific Phobia/Agrobphobia
dataf["Specific Phobia/Agrophobia"]= np.where(dataf["FEAR"]>=2,1,0)

#Acute Stress Disorder
#PTSD feature needs to be answered with a value of greater than 2, and PTSD-2 needs to be answered with a false
dataf["Acute Stress Disorder"] = np.where((dataf["PTSD"]>=2) & (dataf["PTSD-2"]=="0"),1,0)
# print(dataf["Acute Stress Disorder"])

#PTSD
#PTSD feature needs to be answered with a value of greater than 2, and PTSD-2 needs to be answered with a True
dataf["PTSD"] = np.where((dataf["PTSD"]>=2) & (dataf["PTSD-2"]=="1"),1,0)

#GAD
#BLANK feature needs to have a value of greater than 2 or ANX feature needs to have a value of greater than 2
dataf["GAD"]=np.where(dataf["BLANK"]>=2 | (dataf["ANX"]>=2),1,0)

#Conversion/Pain Disorder
#muscle feature needs to have a value greater than 2
#dataf["Conversion/Pain Disorder"]= np.where(dataf["MUSCLE"]>=2,1,0)

#Somatization Disorder
#NEURO feature needs to have a value greater than 2
# dataf["Somatization Disorder"]= np.where(dataf["NEURO"]>=2,1,0)

#Hypochrondriasis
#HYPOCHRON feature needs to have a value of greater than 2
# dataf["HYPOCHRONDRIASIS"]= np.where(dataf["HYPOCHRON"]>=2,1,0)

#Body Dysmoprhic Disorder
#APPEAR FEAR needs to have a value of greater than 2
# dataf["Body Dsymorphic Disorder"]= np.where(dataf["APPEAR FEAR"]>=2,1,0)

#Facitious Disorder
dataf["Facitious Disorder"]= np.where(dataf["FACITIOUS"]>=2,1,0)

#Dissociative Fugue/Depersonalization
#DETACH feature needs to have a value of greater than 2 for this disorder to be activated
dataf["Dissociative Fugue/Depersonalization"]= np.where(dataf["DETACH"]>=2,1,0)

#Dissociative Identity Disorder
#MULTI PERSON feature needs to have a value of greater than 2 for this disorder to be activated
dataf["Dissociative Identity Disorder"]= np.where(dataf["MULTI PERSON"]>=2,1,0)

#Eating Disorder
#Appear Fear needs to have a value og freater than 2 for this disrder to be activated. 
#Eating disorder has a similar condition to body dsymorphic disorder
dataf["Eating Disorder"]= np.where(dataf["APPEAR FEAR"]>=2,1,0)

#Nightmare Disorder
#SLEEP DISORDR needs to classified with a value of greater than 2
dataf["Nightmare Disorder"]= np.where(dataf["SLEEP DISORDR"]>=2,1,0)

#Narcolepsy
#NARCOLEP and SLEEP PARAL-2 feature needs to have a value greater than 2 for this disorder to be activated
dataf["Narcolepsy"]=np.where(dataf["NARCOLEP"]>=2 & (dataf["SLEEP PARAL-2"]>=2),1,0)

#Breathing Related Sleep Disorder
#NARCOLEP and SNORE need to have values of greater than 2 for this disorder to exist
dataf["BR-Sleep Disorder"]=np.where(((dataf["NARCOLEP"]>=2) & (dataf["SNORING"]>=2)),1,0)   
# print(dataf["BR-Sleep Disorder"])

#Sleep Walking
dataf["Sleep Walking"]=np.where(dataf["SLEEP WALK"]>=2,1,0) 

#Pyromania
#PYRO needs to be satisfied with a value of greater than 2 for this disorder to be activated
dataf["Pyromania"]=np.where(dataf["PYRO"]>=2,1,0)

#Trichotillomania
#HAIR LSS needs to be satisfied with a score of greater than 2 for this disorder to be activated
dataf["Trichotillomania"]= np.where(dataf["HAIR LSS"]>=2,1,0)

#Pathological Gambling
#GAMBLE needs to be satisfied with a value of greater than 2 for this disorder to be activated
dataf["Pathological Gambling"]= np.where(dataf["GAMBLE"]>=2,1,0)

#Kleptomania
#STEAL needs to be satisfied with a value of greater than 2 for this disorder to be activated
dataf["Kleptomania"]= np.where(dataf["STEAL"]>=2,1,0)

#Intermittent Eplosive Disorder
#IMPULSV-2 needs to be satisfied with a score of greater than 2
dataf["Intermittent Explosive Disorder"]= np.where(dataf["IMPULSV-2"]>=2,1,0)

#Borderline Personality Disorder
# dataf[" Borderline Sample"]=np.where((dataf["DETACH"]>2 &(dataf["DEPR-1"]>2)),1,0)
dataf["Borderline Personality Disorder"] = np.where(((dataf["DETACH"]>=2) & (dataf["DEPR-1"]>=2) & (dataf["ALONE"]>=2)),1,0)
# print(dataf["Borderline Personality Disorder"])
# dataf.drop(["Border Personality Disorder Sample"],axis=1)

#Narcissistic Personality Disorder
#NARCISSISTIC feature needs to have a value of greater than 2 for thsi disorder to be activated
dataf["Narcissistic Personality Disorder"] = np.where( (dataf["NARCISSISTIC"]>=2),1,0)

#Dependent Personality Disorder
#DEPENDENT feature needs to have a value of greater than 2
dataf["Dependent Personality Disorder"] = np.where( (dataf["DEPENDENT"]>=2),1,0)

#Avoidant Personality Disorder
#DEPENDENT-2 needs to have a value of greater than 2
dataf["Avoidant Personality Disorder"] = np.where( (dataf["DEPENDENT-2"]>=2),1,0)

#Paranoid Personality Disorder
#PARANOID feature needs to have a value of greater than 2
dataf["Paranoid Personality Disorder"] = np.where( (dataf["PARANOID"]>=2),1,0)

#Histronic Personality Disorder
#Either ECCENTRIC or INAPPRO feature needs to have a value of greater than 2
dataf["Histronic Personality Disorder"]=np.where(((dataf["ECCENTRIC"]>=2) | (dataf["INAPPRO"]>=2)),1,0)

#OCD
#OCD feature needs to have a value of 2 or greater for this disorder to activated
dataf["Obssessive Compulsive Disorde"]=np.where((dataf["OCD"]>=2),1,0)

#Antisocial Behavior
#ANTISOCIAL-1 needs to have a value of 2 or greater for this disorder to be activated
dataf["PANIC DISORDER"]= np.where(dataf["ANTISOCIAL-1"]>=2,1,0)

#Schzioid Personality Disorder
dataf["Schzoid Personality Disorder"]= np.where(((dataf["SCHIZOAFFECTIVE"]>=2) & (dataf["COLD"]>=2)),1,0)

# #Feature Engineering
# sns.pairplot(dataf.sample(2))
# sns_plot.savefig("pairplot.png")

# plt.clf() # Clean parirplot figure from sns 
# Image(filename='pairplot.png') # Show pairplot as image

dataf.dtypes
dataf.drop(["Patient Name"],axis=1)
# print(dataf.iloc[:,52:88])
X = dataf.iloc[:,1:53]
y = dataf.iloc[:,53:90]

# K-fold Iterative Stratification
k_fold = IterativeStratification(n_splits=40, order=1)
for train_index, test_index in k_fold.split(X, y):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]
    # classifier.fit(X_train, y_train)
    # result = classifier.predict(X_test)


mlb = MultiLabelBinarizer()

start=time.time()
classifier = BinaryRelevance(
    classifier =  RandomForestClassifier(n_estimators=100,criterion='gini'),
    require_dense = [False, True]
)

classifier.fit(X_train, y_train)
predictions =classifier.predict(X_test)

# def Accuracy(y_test, predictions):
#     temp = 0
#     for i in range(y_test.shape[0]):
#         temp += sum(np.logical_and(y_test[i], predictions[i])) / sum(np.logical_or(y_test[i], predictions[i]))
#     return temp / y_test.shape[0]
    
# Accuracy(y_test, predictions)
from sklearn.metrics import recall_score
r=recall_score(predictions,y_test,average='samples')
print("the recall score is",recall_score)
l=precision_score(y_test, predictions, average='samples') 
print("The precision score for mental disorder multi-label classification is",r)
br_f1=metrics.f1_score(y_test, predictions, average='macro')
br_f2=metrics.f1_score(y_test, predictions, average='micro')
br_f3=metrics.f1_score(y_test, predictions, average='weighted')
br_f4=metrics.f1_score(y_test, predictions, average='samples')
br_hamm=metrics.hamming_loss(y_test,predictions)

print('Binary Relevance F1-score:',round(br_f1,3))
print('Binary Relevance F1-score:',round(br_f2,3))
print('Binary Relevance F1-score:',round(br_f3,3))
print('Binary Relevance F1-score:',round(br_f4,3))
print('Binary Relevance Hamming Loss:',round(br_hamm,3))

#Learning Curve
from sklearn.model_selection import learning_curve
from sklearn.metrics import roc_auc_score
from sklearn.metrics import label_ranking_loss 
from sklearn.metrics import coverage_error 
from sklearn.metrics import average_precision_score
average_precision = average_precision_score(y_test, predictions)
print(coverage_error(y_test, predictions))
# print(label_ranking_loss(y_test, predictions ))

#Decision Trees
# Generating 100 subsets of the training data with 100 randomn instances
n_trees = 1000
n_instances = 30

mini_sets = []

rs = ShuffleSplit(n_splits=n_trees, test_size=len(X_train) - n_instances, random_state=42)
for mini_train_index, mini_test_index in rs.split(X_train):
    X_mini_train = X_train.iloc[mini_train_index]
    y_mini_train = y_train.iloc[mini_train_index]
    mini_sets.append((X_mini_train, y_mini_train))

# Label Powerset
classifier = LabelPowerset(
    classifier = RandomForestClassifier(),
    require_dense = [False, True]
)

start=time.time()
classifier.fit(X_train, y_train)
print('training time taken: ',round(time.time()-start,0),'seconds')
start=time.time()
predictions=classifier.predict(X_test)
print('prediction time taken: ',round(time.time()-start,0),'seconds')


lp_f1=metrics.f1_score(y_test, predictions, average='micro')
lp_hamm=metrics.hamming_loss(y_test,predictions)
print('Label Powerset F1-score:',round(lp_f1,3))
print('Label Powerset Hamming Loss:',round(lp_hamm,3))

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

# LogReg_pipeline = Pipeline([
#                 ('clf', OneVsRestClassifier(LogisticRegression(solver='sag'), n_jobs=-1)),
#             ])
# LogReg_pipeline.fit(X_train, y_train)
#   # calculating test accuracy
# prediction = LogReg_pipeline.predict(X_test)
# from sklearn.metrics import classification_report, confusion_matrix
# print('Test accuracy is {}'.format(accuracy_score(prediction,y_test)))


# initialize classifier chains multi-label classifier
classifier = ClassifierChain(LogisticRegression())

# Training logistic regression model on train data
# classifier.fit(X_train, y_train)

# # predict
# predictions = classifier.predict(x_test)

# # accuracy
# print("Accuracy = ",accuracy_score(y_test,predictions))
# print("\n")
