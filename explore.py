# 1. yes, i can explain a boolean filter, and it's using and, or, and not (booleans) to filter through content, specifically utilizing the fact that python 'stops' if a statement is true and 'continues' if false.
# 2. the difference between df["revenue"] and df[["revenue"]] is that the former is a series and the latter is a dataframe, and the distinction is needed when several columns of info has to be selected, which would suit a dataframe better.
# 3. i would say that pandas is significantly faster than excel when it comes to tasks like this, so pandas is better than excel at the moment.

# exercise 1: load it
import pandas as pd
df = pd.read_csv('data/retail_sales.csv')
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)
print()

# exercise 2: filter by region 
south = df[df['region'] == 'South']
print(len(south))
print(south.head())
print()

# # exercise 3: top 5 by revenue
sorting = df.sort_values('revenue', ascending=False).head(5)
print(sorting)
print()

# # exercise 4: 2-condition filter
big_south = df[(df['region']=='South') & (df['revenue']>1000)]
print(big_south)
print()

# # exercise 5: a new column
df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())
print(df['per_unit'].mean())
print()

# # exercise 6: unique values
print(df['region'].unique())
print(df['region'].value_counts())
print()

# exercise 7: select columns
df2 = df[['region', 'product', 'revenue']]
print(df2)
print(df2.shape)

# exercise 8: save
# df.to_csv('data/explored.csv', index=False)
