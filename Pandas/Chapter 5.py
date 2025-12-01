# Code from book
import pandas as pd
import numpy as np

# Series
l = ['a','b','c','d','e']
l2 = ['a','b','c','d','q']
data = np.arange(5)
aS = pd.Series(data, index = l)               # 0-9 in series with letters as index
aS2 = pd.Series(np.arange(3,12,2), index = l2)# odd numbers 3-11 inclusive

# print(aS[['a', 'c']])      # print selecte items in a list of 1 item lists
# print(aS[aS>5])            # print items in aS where the values are > 5

# print('f' in aS, 'q' in 'aS')   # prints True False

# print(pd.isnull(aS))    # boolean list of whether values are null from function call
# print(aS.isnull())      # Same as previous, but an "instance" call rather than function call

# print(aS+aS2)   # Prints NaN where index does not exist in other series, data aligns automatically

aS2.index = [1,2,3,4,5]     # changes the index. Note: indices can be alphanumeric combos

# DataFrames
data = {"key": ["b", "b", "a", "c", "a", "a", "b"], "data1": [1, 2, 3, 4, 5, 6, 7]} # nested dictionariesworks, keys mus be unique; outer is columns
df  = pd.DataFrame(data)
# df  = pd.DataFrame(data, columns=['data1', 'key'])   # changing order of columns

df2 = pd.DataFrame({"key": ['a', 'b', 'c'],'data2': [10, 20, 30]})

# print(df['data1'])  # a Series in the DataFrame can be retrieved

df['data1'] = 5 # changes all values in the column to 5.
df['data1'] = np.arange(7.) # must match the length of the data1 series and makes values floats.

df['new'] = df.key == 'b' # boolean values in new column. If the key was 'b', the value is true
del(df['new']) # delete a column
df.T # transposes the dataframe (does not change df at this point)
# df2 = pd.DataFrame(data, index = ['1', '3', '5']) length of data must match length of index.
df.index.name = 'index'
df.columns.name = 'headers'
df.values # Returns a list of lists ie list with series in it.
# print(df.values)

# *****   Indices    *****
# indices can not be individually changed.  Must change the complete set.
# Pandas indices can contain duplicate labels.

# *****   Essential Functionality   *****
# reindex([new index]) method new index must be the same length as old index.
# reindex() method object allows for interpolation between values.  '
#       method = 'ffill' forward fill values. ie if a value is blank, it uses the previous value.
#                'bfill' backwards fills.
#       fill_value = 'whatever'

# *****   Dropping Entries from an Axis   (axis = 1 is columns, axis = 0 is rows)   *****
# new_dataframe =old_datframe.drop([list of columns or rows to drop])
# old_datframe.drop([list of columns or rows to drop], inplace = True ) setting the option inplace = True, 
#       will do the same thing without creating a new copy, therby destroying the data dropped.

# *****   Indexing, selection and filtering   *****
# slicing with labels includes all labels listed.
# print(df[df['data1']>3]) # returns only those rows where df>3.  Returns all columns
# print(df<5) # boolean series if all values in df are numeric.

# Select subset of rows and columns with
# loc[[rowss to select], [columns to select]] used with labels
# iloc used with integers
# print(df.loc[:,'data1']) # prints all rows in column 'data1'
# print(df.loc[1])    # prints row 1 by column as a series
# print(df.iloc[1,:]) # does the sAME THIng but with integer indices

# if you have an axis index containing integers, data selection will always be label-oriented.

# *****   Arithmetic and Data Alignment   *****
# adding two series is like an outer join (ie all rows and columns from both series) where only exist in 1, NAN is returned.
# df.add(df2,fill_value=0) will put zeros where only column or row existed in one of df or df2.
# 1/df is the same as df.rdiv(1) the r represents reciprocal.
# methods: add,sub, div, floordiv, mul, pow

# *****   Operations between DataFrame and Series   *****
# By default, arithmetic between DataFrame and Series matches the index of the Series 
#   on the dataFrame 's columns, broadcasting down the rows

# Note: axis = 0 is the same as axis ='index'

# *****   Function Application and Mapping   *****
# Universal functions (ufunc) like np.abs(df)  <-- element wise absoulte value of dataframe.
def f(x):
    return pd.Series([x.min(), x.max(), x.max()-x.min()], index = ['min', 'max', 'range'])

df = pd.DataFrame(np.random.randn(4,3), columns = list('bca'), index = ['ab', 'bc', 'yk', 'sk'])
print(df)
# print(df.apply(f)) # default will give the min/max/range of each column


format = lambda x: '%.2f' % x
# print(df.apply(f, axis = 'columns').map(format)) # gives the min/max/range of each row

# *****   Sorting and Ranking   *****
# print(df.sort_index()) # Sorts the dataset based on the index
# print(df.sort_index(axis = 1))

# Duplicate inidices
# df.index.is_unique returns True if you have unique inidices

# *****   Summarizing and Computing Descriptive Statistics   *****
# df.sum() returns column summs (axis = 1 or axis = 'columns') will summ the rows
# Note: 1 + NAN = 1, NAN are treated like zeros unless skipna=False option is used
# df.idxmax, df.idxmin return index of max/min - argmax(),argmin() return integer values of the index

# print(df.cumsum()) # cummulative sum by column
print(df.describe())  # Summary statistics for each column
# userfull stats: var, std, skew, median, count, pct_change ....

# *****   Correlation and Covariance   *****
# Computes correlation of the overlapping, non-NA, aligned by index values in 2 series
# print(df['a'].corr(df['c']))
# print(df.a.corr(df.c)) # this and previous line yield same result.
print(df.corr())
print(df.corrwith(df.a))

# *****   Unique Values, Value counts, and membership   *****
# df.uniques() returns the unique values in a series
# df.value_counts() returns series with value frequencies
# mask - df.isin(['b', 'c']) mask = a boolean list of whether the value is either b or c.
# df[mask] then returns only the True

# Histogram: histogram_table = df.apply(pd.value_counts).fillna(0)