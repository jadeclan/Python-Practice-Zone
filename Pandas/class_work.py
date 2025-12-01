import pandas as pd

df1 = pd.DataFrame({"key1":["b", "b", "a", "c", "a", "a", "d"],'key2': ['a', 'a', 'b', 'b', 'c', 'c', 'd'],"data1":[1, 2, 3, 4, 5, 6, 7]})
df2 = pd.DataFrame({"key1": ['a', 'b', 'c', 'e'],'key2': ['a', 'a', 'b', 'd'],'data2': [10, 20, 30, 40]})
joined = pd.merge(df1, df2, on=["key1", 'key2'], how='inner') 
print(joined)

# Exercise: matching on different column names: Match where left table’s key1 matches right table’s key2.
# merge 2 tables at a time.
joined = pd.merge(df1, df2, left_on="key1", right_on='key2', how='inner') 
print(joined)

joined = pd.merge(df1,df2, on='key1', how='inner', suffixes =('_left','_right'))
print(joined)
