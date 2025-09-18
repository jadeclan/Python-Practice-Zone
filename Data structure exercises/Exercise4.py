"""
Exercise: Associating values with and without dict
We want to convert months’ names to their numbers 
(i.e. “January” → 1, “February” → 2, etc.)
Write a function that accomplishes this. Do it two different ways:
1   Using only lists
2   Using a dictionary
"""
months = ['jan','feb','mar', 'apr']
hash_values = [1, 7, 3, 4]

months_dictionary = {'jan':1,'feb':7,'mar':3, 'apr':4}
 
def main():
    month_chosen = 'feb'

    # Finding the month with lists
    index = get_index_of(month_chosen)
    if index < 0:
        print(f"{month_chosen} was not found.")
    else:
        print(f"The month of {month_chosen} has a hash value of {hash_values[index]}.")

    # Finding the month with a dictionary
    if month_chosen in months_dictionary:
        print(f"The hash value for {month_chosen} is {months_dictionary[month_chosen]}.")
    else:
        print(f"{month_chosen} was not found.")   

def get_index_of(month: str) -> int:

    if month in months:
        return months.index(month)
    else:
        return -1
    
main()