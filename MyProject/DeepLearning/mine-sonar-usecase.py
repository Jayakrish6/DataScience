# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

def read_dataset():
    df = pd.read_csv("D:\\FADVProject\\Documents\\Study\\DataScience\\DataSets\\sonar-data-set\\sonar.csv")
    
    x = df[df.columns[0:60]].values
    y = df[df.columns[60]]

    #Encode the dependent variable
    encoder = LabelEncoder()
    encoder.fit(y)
    y = encoder.transform(y)
    Y = one_hot_encode(y)
    print(x.shape)
    return (x, Y)
    
#Define encoder function
def one_hot_encode(labels):
    n_labels = len(labels)
    n_unique_labels = len(np.unique(labels))
    one_hot_encode = np.zeros((n_labels, n_unique_labels))
    one_hot_encode[np.arange(n_labels), labels] = 1
    return one_hot_encode

x, Y = read_dataset()

#Shuffle the dataset
x, Y = shuffle(x, Y, random_state=1)

#Convert the dataset into train and test part
train_x, test_x, train_y, test_y = train_test_split(x, Y, test_size=0.20, random_state=415)

#Inspect teh training and testing data
print(train_x.shape)
print(train_y.shape)
print(test_x.shape)

#Define the important parameters
learnign_rate = 0.3
training_epochs = 1000
cost_history = np.empty(shape=[1], dtype=float)
#n_dim = 