import pandas as pd

df = pd.read_csv('http://bit.ly/kaggletrain')

df['sexMale'] = df['Sex'].map({'male': 1, 'female': 0})

print(df[['Sex', 'sexMale']].head())

#  s1 = pd.Series(range(2, 7), name='s2')
