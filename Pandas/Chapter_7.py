# Chapter_7 Code examples
import pandas as pd
import numpy  as np
"""
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
"""

# df = pd.DataFrame({
# 'degree': ['DS', 'DS', 'DS', 'BA', 'BA', 'BA'],
#      'num_courses': [3, 4, 5, 3, 4, 5],
#      'num_respond': [20, 40, 75, 100, 40, 10]
#      })

# def weighted_avg_courses(group_df: pd.DataFrame) -> float:
#     weighted_sum = (group_df['num_courses'] * group_df['num_respond']).sum()
#     return weighted_sum / group_df['num_respond'].sum()

# print(df.groupby('degree').apply(weighted_avg_courses))


# Using groupby and .agg, print out a series showing each customer and whether 
# or not they purchased “ram”:
# df = pd.DataFrame({
#         'date': ['2025-03-01','2025-03-01', '2025-03-02', '2025-03-02', 
#                  '2025-03-03', '2025-03-03'],
#         'customer': ['alice', 'bob', 'alice', 'charley', 'bob', 'charley'],
#         'product': ['motherboard', 'ram', 'ram', 'ssd', 'ssd', 'ssd']
# })

# def purchased_ram(products: pd.Series) -> bool:
    
#     return 'ram' in products.values
# print(df.groupby('customer')['product'].agg(purchased_ram))

# def purch(products:pd.Series) -> bool:
#     return 'ram' in products.values
# print(df.groupby('customer')['product'].apply(purch))

# print(df.groupby('customer')['product'].apply(lambda product: "ram" in product.values))
# def purch2(products:df.DataFrame) -> bool:
#     return 'ram' in products['product'].values
# print(df.groupby('customer').apply(purch2))

# Compute a series showing the range of prices (min to max) by month
df = pd.DataFrame({
    'date': ['2/25/2025', '2/26/2025', '2/27/2025', '2/28/2025', '3/3/2025',
             '3/4/2025', '3/5/2025', '3/6/2025', '3/7/2025', '3/8/2025'],
    'Open': [98.7, 100.3, 101.7, 103.2, 104.1, 105, 106.5, 107, 108.3, 109.7],
    'High': [101.2, 102.8, 104, 105.5, 106.3, 107.1, 108.2, 109, 110.5, 111.2],
    'Low': [97.5, 99, 100.5, 101.8, 102.7, 103.8, 104.9, 105.7, 106.8, 108.1],
    'Close': [100.3, 101.7, 103.2,104.1, 105, 106.5, 107, 108.3, 109.7, 110.4]})

df['date'] = pd.to_datetime(df['date'])
# df.set_index('date', inplace=True)
def price_range(group_df: pd.DataFrame) -> (float, float):
    return  f'${group_df['Low'].min():.2f} - ${group_df['High'].max():.2f}'

df['month'] = df['date'].dt.month
group = df.groupby('month')

print(group.apply(price_range))


# year =pd.Series([2019,2020,2020,2017,2015,2015,2017,2016,2016,2016,2016,2016,2018,2016,2020,2016,2019,2018,2018,2015,2019,2016,2018,2020,2020,2019,2016,2018,2015,2018,2020,2016])
# dept =pd.Series(['hardware', 'seasonal', 'hardware', 'houseware', 'houseware','seasonal', 'houseware', 'houseware', 'seasonal', 'seasonal','seasonal', 'hardware', 'houseware', 'hardware', 'hardware', 'hardware', 'houseware', 'hardware', 'houseware', 'hardware','houseware', 'houseware', 'seasonal', 'hardware', 'seasonal','seasonal', 'houseware', 'hardware', 'hardware', 'hardware', 'seasonal', 'houseware'])
# product =pd.Series(['paint', 'bbq', 'tablesaw', 'nightstand', 'frying pan', 'bbq', 'rug', 'nightstand',
#             'snow shovel', 'rake', 'bbq', 'nails', 'rug', 'tablesaw', 'nails', 'paint',
#             'frying pan', 'nails', 'frying pan', 'nails', 'nightstand', 'frying pan', 'lawn chair',
#             'paint', 'rake', 'lawn chair', 'hanging art', 'tablesaw', 'tablesaw', 'paint', 'snow shovel', 'rug'])
# sales = pd.Series([11487, 13690, 1775, 12187, 9624, 4696, 17884, 17977, 18641, 15487,6054, 9559, 19366, 1679, 1973, 14835, 5532, 1586, 9559, 14959,5729, 3262, 18608, 5470, 16419, 15731, 17005, 2682, 10548, 11186, 15068, 12861])
# rating = pd.Series([67, 74, 70, 75, 77, 74, 77, 99, 51, 74,98, 65, 79, 89, 62, 60, 62, 76, 55, 53,86, 75, 95, 58, 83, 81, 86, 92, 97, 100, 75, 68])
# data =pd.DataFrame({'year': year, 'dept': dept, 'product': product, 'sales': sales, 'rating': rating})  
# # Using the sales data, create a pivot table that shows: dept & product on the rows, year and “> 85 rating” along the columns
# # total sales and average rating as the values. 


# data['> 85 rating'] = data['rating'] > 85
# pivot_table = pd.pivot_table(data, 
#                              index=['dept', 'product'], 
#                              columns=['year', '> 85 rating'], 
#                              values=['sales', 'rating'], 
#                              aggfunc={'sales': np.sum, 'rating': np.mean},
#                              fill_value=0)
# print(pivot_table)
# # Now index the total sales for houseware / rugs in 2016 with < 85 quality rating.
# total_sales_rugs_2016 = pivot_table.loc[('houseware', 'rug'), (2016, False), 'sales']
# print(f'Total sales for houseware/rugs in 2016 with < 85 quality rating: {total_sales_rugs_2016}')



# Group Operations
# grouping by one column
# df =pd.DataFrame({'day': ['mon', 'mon', 'tue', 'tue', 'wed', 'wed', 'thu', 'thu', 'fri', 'fri'],
#                   'data':[1,2,3,4,5,6,7,8,9,10]})
# print(df)
# grouped =df.groupby('day')
# grouped['data']
# print(grouped.mean())

# year =pd.Series([2019,2020,2020,2017,2015,2015,2017,2016,2016,2016,2016,2016,2018,2016,2020,2016,2019,2018,2018,2015,2019,2016,2018,2020,2020,2019,2016,2018,2015,2018,2020,2016])
# dept =pd.Series(['hardware', 'seasonal', 'hardware', 'houseware', 'houseware','seasonal', 'houseware', 'houseware', 'seasonal', 'seasonal','seasonal', 'hardware', 'houseware', 'hardware', 'hardware', 'hardware', 'houseware', 'hardware', 'houseware', 'hardware','houseware', 'houseware', 'seasonal', 'hardware', 'seasonal','seasonal', 'houseware', 'hardware', 'hardware', 'hardware', 'seasonal', 'houseware'])
# product =pd.Series(['paint', 'bbq', 'tablesaw', 'nightstand', 'frying pan', 'bbq', 'rug', 'nightstand',
#             'snow shovel', 'rake', 'bbq', 'nails', 'rug', 'tablesaw', 'nails', 'paint',
#             'frying pan', 'nails', 'frying pan', 'nails', 'nightstand', 'frying pan', 'lawn chair',
#             'paint', 'rake', 'lawn chair', 'hanging art', 'tablesaw', 'tablesaw', 'paint', 'snow shovel', 'rug'])
# sales = pd.Series([11487, 13690, 1775, 12187, 9624, 4696, 17884, 17977, 18641, 15487,6054, 9559, 19366, 1679, 1973, 14835, 5532, 1586, 9559, 14959,5729, 3262, 18608, 5470, 16419, 15731, 17005, 2682, 10548, 11186, 15068, 12861])
# rating = pd.Series([67, 74, 70, 75, 77, 74, 77, 99, 51, 74,98, 65, 79, 89, 62, 60, 62, 76, 55, 53,86, 75, 95, 58, 83, 81, 86, 92, 97, 100, 75, 68])
# data =pd.DataFrame({'year': year, 'dept': dept, 'product': product, 'sales': sales, 'rating': rating}) 
# print(data) 

# print(data.groupby('dept')['sales'].sum())

# total_sales = data.groupby(['dept', 'year'])['sales'].sum()
# print(total_sales)
# # print houseware sales for 2015
# print(total_sales[('houseware',2015)])

# # You can supply a list of aggregations
# # Alt syntax for aggregation
# # data.groupby('dept'['sales'].agg('sum'))
# print(data.groupby('dept')['sales'].agg(['mean', 'sum']))
# # Multiple aggregations on multiple columns
# grouped = data.groupby('dept')[['sales','rating']].agg(['mean', 'sum'])
# print(grouped)

# # using a dictioanary to specify different aggregations for each column
# print(data.groupby('dept')[['sales','rating']].agg({'sales':'sum', 'rating':['min', 'max']}))

# def custom_range(series: pd.Series) -> float:
#     return series.max() - series.min()

# group= data.groupby('dept')['sales'].agg(custom_range)
# # print(group)
# def custom_agg(df: pd.DataFrame) -> float:
#     # get total sales for all products with rating > 60
#     return df.loc[data['rating'] > 60, 'sales'].sum()
    
# print(data.groupby('dept').apply(custom_agg))

