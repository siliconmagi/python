#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 16:46:46 2017

@author: zeal
"""

import pandas as pd

startYear = 2004
endYear = 2014
make = 'Ford'
model = 'F-150'
trim = 'Crew Cab'
ex = pd.DataFrame
sd = pd.read_csv('./mvlTrim.csv')
fd = pd.read_excel('./fitmentExp.xlsx')

print(type(sd))
#print(sd['Year'].dtype)
print(sd.dtypes)

# Sort and return new dataframe
sd = sd.sort_values(by=['Make'], ascending=[True])
sd = sd.sort_values(by=['Year'], ascending=[True])
print(sd)

#sd['Crew Cab'] = sd['len'].apply(lambda x: 'True' if x > 80 else 'False')
# select rows return as new dataframe
e1 = sd.loc[(sd['Year'] > (startYear -1)) & (sd['Year'] < (endYear +1)) & (sd['Make'] == make) & (sd['Model'] == model) & (sd['Trim'].str.contains(trim))]



# drop duplicates
e2 = e1.drop_duplicates()
print(e2)

# write csv
sd.to_csv('mvl.csv',index=False,header=True)