import pandas as pd

orders = pd.read_table('http://bit.ly/chiporders')

print(orders.dtypes)
print(orders.head())

# to do math on item_price:
# convert from object to float
orders2 = orders.item_price.str.replace('$', '').astype(float).mean()
print(orders2)

# convert true:false to 1:0
orders2 = orders.item_name.str.contains('Chicken')
print(orders2.head())
print(orders.item_name.str.contains('Chicken').astype(int).head())
