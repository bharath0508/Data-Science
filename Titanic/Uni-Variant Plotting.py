#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 12:18:32 2019

@author: bharath
"""

import os
import pandas as pd
import seaborn as sns

#returns current working directory
os.getcwd()
#changes working directory
os.chdir("/Users/bharath/Desktop/Folder/Data Science/Projects/titanic")

titanic_train = pd.read_csv("train.csv")

#EDA
titanic_train.shape
titanic_train.info()
#.describe() gives the statistical information continuous columns
titanic_train.describe()

#Convert pclass number to categoric
titanic_train['Survived'] = titanic_train['Survived'].astype('category')
titanic_train['Pclass'] = titanic_train['Pclass'].astype('category')
titanic_train['Sex'] = titanic_train['Sex'].astype('category')
titanic_train['Embarked'] = titanic_train['Embarked'].astype('category')

titanic_train.describe()

#explore univariate continuous feature
print(titanic_train['Fare'].mean())
print(titanic_train['Fare'].median())
print(titanic_train['Fare'].quantile(0.25))
print(titanic_train['Fare'].quantile(0.75))
print(titanic_train['Fare'].std())
titanic_train['Fare'].describe()
titanic_train['SibSp'].describe()

#explore univariate continuous features visually
sns.boxplot(x='Fare', data=titanic_train)
#distplot function is very useful to display density plot with histogram
sns.distplot(titanic_train['Fare'], kde=False)
sns.distplot(titanic_train['Fare'], bins=10, kde=False)
sns.distplot(titanic_train['Fare'], bins=100, kde=True)
#kdeplot is for density plot
sns.kdeplot(data=titanic_train['Fare'])
sns.kdeplot(data=titanic_train['Fare'], shade=True)

#explore univariate categorical feature
#Check what is freq(ency)
titanic_train['Survived'].describe()
titanic_train['Survived'].value_counts()
pd.crosstab(index=titanic_train["Survived"], columns="count")
pd.crosstab(index=titanic_train["Pclass"], columns="count")  
pd.crosstab(index=titanic_train["Sex"],  columns="count")

#explore univariate categorical features visually
sns.countplot(x='Survived',data=titanic_train)
sns.countplot(x='Pclass',data=titanic_train)