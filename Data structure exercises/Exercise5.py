"""
Exercise: loop through a dictionary
Consider the following dictionary:
    work_shifts = {
        'Alice': 'Weekdays',
        'Bob': 'Weekdays',
        'Charly': 'Weekends',
        'Denise': 'Weekdays'
    }
Loop through the key-value pairs to populate two new lists: a list of people working weekends, and a list of people working weekdays.
Now try creating both lists using list comprehensions.
"""
work_shifts = {
        'Alice': 'Weekdays',
        'Bob': 'Weekdays',
        'Charly': 'Weekends',
        'Denise': 'Weekdays'
    }

def main():
    weekenders = []
    weekdayers = []

    for key in work_shifts:
        if work_shifts[key] == 'Weekdays':
            weekdayers.append(key)
        else:
            weekenders.append(key)

    print(f"The weekenders are: {weekenders}.\nThe weekdayers are: {weekdayers} ")

    # In class method of doing the same thing
    weekends = []
    weekdays = []
    for name, shift in work_shifts.items():
        if shift == 'Weekends':
            weekends.append(name)
        else:
            weekdays.append(name)

    print('weekends:', weekends)
    print('weekdays:', weekdays)
main()
