#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:10:54 2019

@author: bharath
"""

import pandas as pd
import os
from sklearn import tree, model_selection

g_train = pd.read_csv('/Users/bharath/Desktop/Data Science/Projects/ghouls-goblins-and-ghosts-boo/train.csv')
g_test =pd.read_csv('/Users/bharath/Desktop/Data Science/Projects/ghouls-goblins-and-ghosts-boo/test.csv') 

def conv_type(type):
    if (type=='Ghoul'):
        return 1
    elif (type=='Goblin'):
        return 2
    elif (type=='Ghost'):
        return 3
  
    
    g_train['type1'] = g_train['type'].map(conv_type)
    g_train['type1'].head()
    g_train.info()
    g_train1 = g_train.drop('type',axis=1)
g_test['type1'] = 0

g_total = pd.concat([g_train1,g_test])

g_total1 = pd.get_dummies(g_total, columns=['color'])
g_total2 = g_total1.drop('id',axis =1)
g_total2.info()
g_train1.info()
X_train = g_total2[0:g_train1.shape[0]]
y_train = g_train1['type1']

tree_estimator = tree.DecisionTreeClassifier()
tree_estimator.fit(X_train,y_train)

cv_scores2 = model_selection.cross_val_score(tree_estimator, X_train, y_train, cv=10)
print(cv_scores2)

X_test = g_total2[g_train1.shape[0]:]
X_test.info()

g_test['type1'] = tree_estimator.predict(X_test)
g_test.info()

def conv_type1(type):
    if (type==1):
        return 'Ghoul'
    elif (type==2):
        return 'Goblin'
    elif (type==3):
        return 'Ghost'
    g_test['type'] = g_test['type1'].map(conv_type1)

g_test.info()
g_test.drop('type1',axis=1,inplace=True)

os.chdir('/Users/bharath/Desktop/Data Science/Projects/house-prices-advanced-regression-techniques')
g_test.to_csv('submission1.csv', columns=['id','type1'],index=False)