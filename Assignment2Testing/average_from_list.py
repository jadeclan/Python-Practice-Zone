# There will be no headers in the list sent to this function, just key-value pairs
data=[
        {'name':'james', 'day':'wed', 'score':22.5, 'sex':'m', 'age':6},
        {'name':'magid', 'day':'tue', 'score':18.5, 'sex':'m', 'age':12},
        {'name':'james', 'day':'tue', 'score':21, 'sex':'f', 'age':23}
        ]

# Figure out what each key is   
key_type = {}
keys = []
for line in data:
    for key in line:
        if key not in keys:
            keys.append(key)

for key, value in data[0].items():
    if isinstance(value, float) or isinstance(value, int):
        key_type[key] = 0
    else:
        key_type[key] = 1

for key in keys:
    # Calculate averages where appropriate, frequencies otherwise
    if key_type[key] ==  0:
        entries = [line[key] for line in data]
        average = sum(entries)/len(entries)
        print(f'The average {key} was {average:.1f}.')
    else:
        # we need the highest frequency
        counts = {}
        most_common_item = None
        highest_count = 0
        for line in data:
            if line[key] not in counts:
                counts[line[key]] = 1
            else:
                counts[line[key]] += 1
        for key, value in counts.items():
            if value > highest_count:
                highest_count = value
                most_common_item = key
        print(f'{most_common_item}  occured {highest_count} times.')

""" Your print out should look like this:
James was the most common name, it occured 2 times.
tue was was the most common date, it occured 2 times.
the average age was: 20.7
There were more males than any other desicgnation
the average hours to complete this nonsense was 13.7 hours.
"""