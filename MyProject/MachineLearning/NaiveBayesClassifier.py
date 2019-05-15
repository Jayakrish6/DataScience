# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns;sns.set() 
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import confusion_matrix

data = fetch_20newsgroups()
data.target_names

