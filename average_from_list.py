test_data=[
        ['name','date', 'age', 'sex'],
        ['james','wed',22.5, 'm'],
        ['magid', 'tue',18,'m'],
        ['james', 'tue', 21, 'f']
    ]

# TODO: figure whats in each column
item = test_data[1]
for field in item:
    print(f'{field} is a float is {isinstance(field, float)}.')
    print(f'{field} is a int is {isinstance(field, int)}.')

sum = 0
count = 0
for line in test_data:
    count += 1
    if line != test_data[0]:
        sum += line[2]
aver = sum/(count-1)

print(f'The average is: {aver:.2f}.')
