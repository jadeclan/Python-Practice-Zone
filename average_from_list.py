test_data=[
        ['name', 'date', 'age', 'sex', 'hour'],
        ['james', 'wed', 22.5, 'm', 6],
        ['magid', 'tue', 18.5,'m', 12],
        ['james', 'tue', 21.0, 'f', 23]
    ]

# TODO: figure whats in each column
#item = test_data[1]
#for field in item:
 #   print(f'{field} is a float is {isinstance(field, float)}.')
  #  print(f'{field} is a int is {isinstance(field, int)}.')

counts = {}
for item in test_data:
    if item != test_data[0]:
        if item[3] in counts:
            counts[item[3]] += 1
        else:
            counts[item[3]] = 1

most_common_item = None
highest_count = 0

for item, count in counts.items():
    if count > highest_count:
        highest_count = count
        most_common_item = item

print(f'{most_common_item}  occured {highest_count} times.')

""""
sum = 0
count = 0
for line in test_data:
    count += 1
    if line != test_data[0]:
        sum += line[2]
aver = sum/(count-1)

print(f'The average is: {aver:.2f}.')
"""

""" Your print out should look like this:
James was the most common name, it occured 2 times.
tue was was the most common date, it occured 2 times.
the average age was: 20.7
There were more males than any other desicgnation
the average hours to complete this nonsense was 13.7 hours.
"""