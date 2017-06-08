import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number

print('hello')
print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
#  print('Matplotlib version ' + matplotlib.__version__)
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]
BabyDataSet = list(zip(names,births))
print(BabyDataSet)
df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])

# write csv
print(df)
df.to_csv('test.csv',index=False,header=True)

# read csv
Location = r'./test.csv'
df = pd.read_csv(Location)
print(df)

# display types
print(df.dtypes)

Sorted = df.sort_values(['Births'], ascending=False)
print(Sorted.head(1))
print(df['Births'].max())

plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()

# Create graph
#  df['Births'].plot()

# Maximum value in the data set
#  MaxValue = df['Births'].max()

# Name associated with the maximum value
#  MaxName = df['Names'][df['Births'] == df['Births'].max()].values

# Text to display on graph
#  Text = str(MaxValue) + " - " + MaxName

# Add text to graph
#  plt.annotate(Text, xy=(1, MaxValue), xytext=(8, 0),
#  xycoords=('axes fraction', 'data'),
#  textcoords='offset points')

#  print("The most popular name")
#  df[df['Births'] == df['Births'].max()]


# Enable inline plotting
#  %matplotlib inline
