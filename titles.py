import pandas as pd
import numpy as np

# read csv
Location = r'./base.csv'
df = pd.read_csv(Location)
print(df)

df.titles = df.titles.str.replace('for', 'fits')
print(df)

lf = df.titles.str.len()
print(lf)

# check char length of df column
df['len'] = np.where(df.titles.str.len() > 80, 'True', 'False')
print(df)

#  ef = re.sub(r'for', 'fits', df)
#  result = re.sub(r'for', 'fits', df)

#  df['titles'] = df['titles'].apply(lambda x: re.sub(r'for', 'fits', x)
#  print(df['titles'])
