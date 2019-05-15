# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression 

#%matplotlib inline

df = pd.read_csv(r'D:\FADVProject\Documents\Study\DataScience\DataSets\USA_Housing.csv')
#print(df.columns)

#sns.pairplot(df)
#sns.distplot(df['Price'])
#sns.heatmap(df.corr(), annot=True)

X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 
        'Avg. Area Number of Bedrooms', 'Area Population']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

lm = LinearRegression()
print(lm.fit(X_train, y_train))
#LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
print(lm.intercept_)
print(lm.coef_)

cdf = pd.DataFrame(lm.coef_, X.columns, columns=['Coeff'])
print(cdf)

from sklearn.datasets import load_boston

boston = load_boston()
print(boston.keys())
print(boston['feature_names'])

#Predictions
predictions = lm.predict(X_test)
print(predictions)

#plt.scatter(y_test,predictions)

#sns.distplot((y_test-predictions))

from sklearn import metrics

print(metrics.mean_absolute_error(y_test,predictions))
print(metrics.mean_squared_error(y_test,predictions))
print(np.sqrt(metrics.mean_squared_error(y_test,predictions)))