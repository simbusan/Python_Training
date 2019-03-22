# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
dataset_pd.read_excel("simbu.xlsx",sheetname=0)
from scipy.stats import pearsonr
stat,p=pearsonr(dataset.Attitude,dataset.Duration)
print(stat,p)



dataset_pd.read_excel("simbu.xlsx",sheetname=0)
dataset12.columns
Y=dataset12.Attitude_towards_the_city
X=dataset12.Duration_of_Residence
import statsmodels.api as sm
X=sm.add_constant(X)
Simple=sm.OLS(Y,X)
result=Simple.fit()
result.summary()


Y=dataset12.Attitude_towards_the_city
X=dataset12[['Duration_of_Residence', 'Importance_attached_to_Weather']]
X=sm.add_constant(X)
Multiple-sm.OLS(Y,X)
result=Simple.fit()
result.summary()

import matplotlib.pyplot as plt
plt.scatter(dataset12.Attitude_towards_the_city,dataset12.Duration_of_Residence)

plt.hist(dataset12.Duration_of_Residence)
plt.hist(dataset12.Importance_attached_to_Weather)
stat,p=pearsonr(dataset12.Duration_of_Residence,dataset12.Importance_attached_to_weather)
print(stat,p)
stat,p=pearsonr(dataset12.Attitude_towards_the_city,dataset12.Duration_of_Residence)
print(stat,p)
