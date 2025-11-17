# Chapter_7 Code examples
import pandas as pd
import numpy  as np

data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef', 'Bacon', 'pastrami','honey ham', 'nova lox'],
                     'ounces': [4,3,12,6,7.5,8,np.nan,5,6]})

meat_to_animal = { 'bacon':'pig', 'pulled pork': 'pig', 'pastrami':'cow', 'corned beef': 'cow', 'honey ham': 'pig', 'nova lox': 'salmon'}

# data = data.dropna() # default is to drop any row that has an NAN in it. 
                     # how='all' <-- all items in row must be NAN
                     # axis=1 looks at the columnar data rather than row.

# print(data[data['food'].str.lower().duplicated()]) # boolean list where True indicates a duplicate.

# add new column, make sure food column is all lowercase, then map to type of animal.
data['animal'] = data['food'].str.lower().map(meat_to_animal)

data.rename(columns={'food' : 'menu item'}, inplace=True) # need to make inplace=True if not creating new DataFrame

# Putting things in bins
bins = [0, 4, 7, 10, 13] # <-- (0,4], (4,7], ... right=False yields [0,4),[4,7),...
group_names = ['extra light', 'light', 'medium',  'heavy'] # These will be the bin names
weight_categories = pd.cut(data['ounces'], bins, labels=group_names)

print(weight_categories.value_counts().sort_index()) # need to sort to get bins in the right order.