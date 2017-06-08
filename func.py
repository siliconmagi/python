"""Obligatory doctype string"""
import re
import pandas as pd

# import csv, any commas in string values will produce parsing error
loc = r'./ttl.csv'
data = pd.read_csv(loc)
print(data)

data.titles = data.titles.str.replace('fits', 'for')
print(data)
