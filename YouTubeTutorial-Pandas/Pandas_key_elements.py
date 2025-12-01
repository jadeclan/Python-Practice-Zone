import pandas as pd
import numpy as np

pd.set_option("display.max_rows", None)

"""
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],
                  columns =['A', 'B', 'C',],
                  index = ['a','x', 'y', 'z'])   # Creates a 2D DataFrame with specified column names and index labels. 
                                             # Default index would be 0,1,2... Default column names would be 0,1,2...
                                             # # in columns= must match column count, # in index= must match row count

# Basic methods and functions to view dataframe information

print(df.head())                             # Displays the first 5 rows of the DataFrame
print(df.head(2))                            # Displays the first two rows of the DataFrame
print(df.tail())                             # Displays the last 5 rows of the DataFrame

print(df.columns.tolist())                   # Displays the column names of the DataFrame in a list format
print(df.index.tolist())                     # Displays the index labels of the DataFrame in a list format

print(df.info())                             # Provides a concise summary of the DataFrame, including data types and non-null counts
print(df.describe())                         # Generates descriptive statistics for numerical columns in the DataFrame

print(df.nunique())
print(df['A'].nunique())        # Print number of unique items in column 'A'

print(df.shape) # prints shape of data
print(df.size) # get the total number of elements in the DataFrame (rows times columns)


coffee = pd.read_csv('./data/coffee.csv')                   # Basic read statement to read in a CSV file.
# results = pd.read_csv('./data/results.csv')
# olympics_data = pd.read_excel('./data/olympics_data.xlsx', sheet_name="results")  # Basic read statement to read in a xlsx file.

# To save a DataFrame as a csv file, use bios.to_csv('test.csv')
# print(coffee.sample(10))    # Will provide 10 rantomly selected rows. Use parameter randomm_state=5 a number to always get same sample

# *****  LOC and ILOC to access specific DataFrame values   ***** (loc slicing is inclusive)
#loc allows to filter by rows and columns.  ie, coffee.loc[#Rows, #Columns]
# print(coffee.loc[0])                          # gives first row of DataFrame in columnar format
# print(coffee.loc[[1,4,6]])                    # note the syntax for getting multiple rows, this time data is desplayed as rows.
# print(coffee.loc[0:3])                        # using slice syntax to get rows 0,1,2 and 3!
# print(coffee.loc[5:8,'Day'])                    # Gets rows 5 to 8 inclusive and only the day column
# print(coffee.loc[5:8, ['Day', 'Units Sold']])   # Gets rows 5 to 8 inclusive and the list of columns

# # ***** ILOC similar to loc but uses integer values for rows and columns ***** (iloc slicing is exclusive)
# print(coffee.iloc[5:8, [0,2]])                  # Note that in this case only rows 5,6,7 are printed

# # ***** To set a specific DataFrame value *****
# coffee.loc[1,'Units Sold'] = 12 # Sets the units sold in row 1 value to 12.
# print(coffee.loc[1:3])
# coffee.loc[1:3,'Units Sold'] = 10
# print(coffee.loc[1:3, ['Day', 'Units Sold']])

# # You can also access specific values using coffee.at[0,'Units Sold'] <-- similar to loc.  coffee.iat[0,3] <-- similar to iloc. can oly pass in 1 row-col combo.

# print(coffee['Day'])  # prints all rows for just the one column
# print(coffee.Day) # also works if doing something with just the one column

# print(coffee.sort_values(["Units Sold", "Coffee Type"], ascending=False)) # sorted by units sold then coffee_type values in descending order
# print(coffee.sort_values(["Units Sold", "Coffee Type"], ascending=[0,1])) # units sold sorted is descending, coffee type sorted in ascending order

# for index, row in coffee.iterrows():  # Sometimes may want to iterate through a datframe row by row, losing memeory efficiency/ performance.
#     print(index)
#     print(row)
#     print("\n\n")
"""

# bios =pd.read_csv('./data/bios.csv')
# ****************************************************
# Filtering data
# print(bios.info())
# Filtering on Height and Weight
# print(bios.loc[bios['height_cm']>215]) # filter based on height > 215. Prints all columns.
# print(bios.loc[bios['height_cm']>215,['name', 'born_country', 'height_cm']]) #only select columns, note closing loc bracket after columns identified
# # shorthand syntax: bios[bios['height_cm']>215] <-- same as line 71 without using loc
# print(bios[(bios['height_cm']>215) & (bios['born_country']=='USA')]) # <-- multi criteria filter
# print(bios[bios['name'].str.contains("james|patrick", case=False)]) # using string method to look for james or patrick (regex syntax being used)
# # other methods bios[bios['born_country'].isin(['Canada', 'USA', 'Barbados'])]
# print(bios[bios['NOC'].isin(['Canada','Barbados']) & (bios['name'].str.startswith('James'))]) # isin() performs only exact case match.

# ****************************************************
# Adding removing columns from dataframe
# coffee = pd.read_csv('./data/coffee.csv')
# coffee['new_colum_name'] = 3.00 # all values in the new column will be 3.00
# print(coffee.head())
# coffee['new_price'] = np.where(coffee['Coffee Type'] == 'Espresso', 3.99, 5.99) # new price will be 2.50 for expresso otherwise 5.99
# print(coffee.head())
# coffee.drop(columns=['new_colum_name'], inplace=True) # Need inplace=True to actually modify the dataframe otherwise we are just modifying a view
#                                                       # coffee = coffee.drop(['new_colum_name']) also works
#                                                       # coffee = coffee[['Day', 'Coffee Type', 'Units Sold', 'new_price']] also works just longer to type

# coffee_new = coffee # coffee new is pointing to the same memeory as coffee. 
# coffee_new =coffee.copy() # now coffee_new is pointing to its own memory space. Use copy if you do not want to modify the original

# coffee.rename(columns={'new_price':'Price'}, inplace=True) # Need to remember t0 set inplace to True to change the actual DataFrame
# coffee['Revenue'] = coffee['Units Sold'] *  coffee['Price']
# print(coffee.head())

# bios =pd.read_csv('./data/bios.csv')
# bios_new = bios.copy()
# bios_new['first_name'] = bios_new['name'].str.split(' ').str[0]
# print(bios_new.head())

# # Working with date/time - First convert the born_date column to a date time object (below we put in a new column)
# bios_new['born_date_time'] = pd.to_datetime(bios_new['born_date'], errors='coerce') #coerce parameter allows to_datetime to handle errors gracefully
# bios_new['year'] = bios_new['born_date_time'].dt.year # other than year: day, month (#), month_name(string), day_name, time
# print(bios_new.head())
# #******* saving the data *****
# bios_new.to_csv('./data/bios_new.csv', index=False) # index =False in order to avoid saving the index column.

# bios['height_category'] = bios['height_cm'].apply(lambda x: 'Short' if x<165 else ('Average' if x < 185 else 'Tall')) # Use of apply to categorize a column
# print(bios.head())

# # Create a custom function to handle a row
# def cat_ath(row):
#     if row['height_cm'] < 175 and row['weight_kg']<70:
#         return 'Lightweight'
#     elif row['height_cm'] < 185 or row['weight_kg']<80:
#         return 'Middleweight'
#     else:
#         return 'Heavyweight'

# # then use apply to applyt the function
# bios['Category'] = bios.apply(cat_ath, axis=1) # axis =1 to specify we are applying on rows
# print(bios.head())

# bios = pd.read_csv('./data/bios.csv')
# noc = pd.read_csv('./data/noc_regions.csv')
# results = pd.read_csv('./data/results.csv')
# *******************************************************
# Merging and concatonating data
# print(noc.head())
# print(noc.info())
# bios_new = pd.merge(bios, noc, left_on='born_country', right_on='NOC', how='left', suffixes=['_bios', '_noc']) # note that a suffix will be added to both column names when both datframes have identically named columns
# bios_new.rename(columns={'region': 'born_country_full'}, inplace=True)
# # print(bios_new[bios_new['NOC_bios'] != bios_new['born_country_full']][['name','NOC_bios', 'born_country_full']]) # to see where athlete competes for a country he was not born in and only 3 columns.

# canada = bios_new[bios_new['born_country_full'] == 'Canada'].copy()
# uk = bios_new[bios_new['born_country_full'] == 'UK'].copy()

# c_and_u = pd.concat([canada,uk]) # pass in a list of data frames to concatonate the dataframes.  will be appended canada then uk.
# print(c_and_u.tail())
# # coffee['new_price'] = np.where(coffee['Coffee Type'] == 'Espresso', 3.99, 5.99) # a numpy where needs values for both true and false conditions
# results['medal'] = results['medal'].where(results['medal'].notna(), other='None') # a pandas where condition keeps original if true, replaces otherwise
# # one = results[results['medal'] == 'Bronze'].copy() # Getting data for only bronze mnedal winners
# # print(bios.info())
# # print(results.info())
# combined_df = pd.merge(results, bios, on='athlete_id', how='left' )
# print(combined_df.iloc[:,:15].head())

# **********************************************
# Handling Null Values
# coffee = pd.read_csv('./data/coffee.csv')
# coffee['Price'] = np.where(coffee['Coffee Type'] == 'Espresso', 3.99, 5.99)
# coffee['Revenue'] = coffee['Units Sold'] *  coffee['Price']
# coffee.loc[[0,1],'Units Sold'] = np.nan # Setting row 0 and 1 column "units Sold' to null for this section
# # df.info() will show how many nulls in each columnn.  df.isna().sum() will give the total count of nan's in the etrire dataframe
# # df.fillna(100)/df.fillna('missing') will replace all nan's with 100/'missing'
# #df.fillna(coffee['Units Sold'].mean()) replaces nans in Units Sold column with the average of the column.
# # df.interpolate() will fill in missing data based on interpolation of the previous non nan and the next nan. ie [1,,,4] would become [1,2,3,4]
# # df.dropna(subset=['Units Sold'])) default drops rows with nan anywhere in them, using subset only drops those rows where "Units Sold" value is nan
# # coffee[coffee['Units Sold'].isna()] gets only the rows with nan in the Units Sold column. coffee[coffee['Units Sold'].notna() is the opposite.
# print(coffee.head())


# **********************************************
# Aggregating Data
# bios = pd.read_csv('./data/bios.csv')
# print(bios.head())
# # let's say we want top cities where the Canadian athletes are from.
# # print(bios[bios['born_country']=='CAN']['born_region'].value_counts()) # Remember df[row condition][columns to show] to filter
# # #When athletes from canada and calgary were born
# # mask = (bios['born_country']=='CAN') & (bios['born_city']=='Calgary')
# # print(bios.loc[mask, 'born_date'])
# # Group by country and determine average height
# # print(bios.groupby(['born_country'])[['height_cm', 'weight_kg']].mean().sort_index())# Groupby requires column names to groupby in the round brackets and a list of columns to display/calculate on
# print(bios.groupby(['born_country']).agg({'height_cm':'mean', 'died_date': 'count'}).sort_values(['died_date'], ascending=False))

# *************************************************
# Pivot Tables
# coffee = pd.read_csv('./data/coffee.csv')
# coffee['Price'] = np.where(coffee['Coffee Type'] == 'Espresso', 3.99, 5.99)
# coffee['Revenue'] = coffee['Units Sold'] *  coffee['Price']
# pivot = coffee.pivot(columns='Coffee Type', index='Day', values='Revenue') # columns will be coffe type, rows will be days and values to show will be revenue
# print(pivot)
# # Note that the order of the rows will be weird.  Also notes that pivot will now be indexed by Day (row) and Coffee Types (columns).
# print(pivot.loc['Monday', 'Latte'])
# print(pivot.iloc[1,1])
# print(pivot.sum()) # columns of pivot table are summed (axis=0 is default)
# print(pivot.sum(axis=1)) # rows of pivot table are summed 

bios = pd.read_csv('./data/bios.csv')
# print(bios.head())
bios['born_date'] = pd.to_datetime(bios['born_date']) # Must convert to datetime object.
# to group people by year they were born
# print(bios.groupby(bios['born_date'].dt.year)[['born_date','name']].count().head(20)) # If born_date not specified, it will not print
# if sorting, its easiest to add  .reset_index().sor_values('name', ascending = False)
# print(bios.groupby(bios['born_date'].dt.year)['name'].count().reset_index().sort_values('name', ascending = False)) # born date does print
# month and year
# need to create two columns first to convert to datetime format.
bios['month'] = bios['born_date'].dt.month
bios['year']= bios['born_date'].dt.year
# print(bios.groupby([bios['year'], bios['month']])['name'].count().reset_index().sort_values(by=['year', 'month'], ascending = [False, True]))

# ****************************************** 
# shift(): ie coffee['yesterday'] = coffee['revenue'].shift(1) so that you could coffee['percent_change']=coffee[revenue']/coffee['yesterday']*100
# rank(): bios['height_rank'] = bios['height_cm'].rank() compares earch athletes height.
# rolling(): coffee
# cumsum(): 
coffee = pd.read_csv('./data/coffee.csv')
coffee['Price'] = np.where(coffee['Coffee Type'] == 'Espresso', 3.99, 5.99)
coffee['Revenue'] = coffee['Units Sold'] *  coffee['Price']
print(coffee)

print(coffee.select_dtypes('float').cumsum())
# revenue last 3 days
# latte = coffee[coffee['Coffee Type'] == 'Latte'].copy()
# latte['3day'] = latte['Units Sold'].rolling(3).sum()
# print(latte)