"""Obligatory doctype string"""
#  check length of strings
#  conditional replace strings
import re
import pandas as pd

# import csv, any commas in string values will produce parsing error
loc = r'./ttl.csv'
data = pd.read_csv(loc)
print(data)

# replace column of strings
data.titles = data.titles.str.replace('fits', 'for')

# list
data['len'] = data.titles.str.len()

# check titles length
data['t2'] = data.titles.str.len() > 80


#  data['t3'] = [(data['len'] > 50)]
#  data.loc[(data['len'] > 50), 'titles']
# return selected values
#  data['t3'] = re.sub(r'[u]','X', data['titles'])
#  data['t3'] = data[data.titles.isin(['wheel'])]
#  data['t3'] = data.titles.filter
#  data['t3'] = data.applymap(re.sub(r'u',r'X',data.titles))

print(data)

# list dataframe info
print(data.info())

# list all headers
print(list(data))

# slice column
print(data.loc[: , 'len'])

# apply method to subset
print(data.loc[:,"len"].mean())

# function
f = lambda x: x+1
print(f(1))
