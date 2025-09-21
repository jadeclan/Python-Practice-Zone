"""
Exercise: set difference and dict difference
Consider the two dictionaries:
    dictA = {'a': 1, 'b': 2, 'd': 3}
    dictB = {'a': 0, 'c': 3, 'd': 3}
Use a set difference operation to identify the set of common keys.
Now reduce dictA to just these keys. Do it 2 different ways:
1   Using a loop
2   Using a dictionary comprehension
"""
# Global variables
dictA = {'a': 1, 'b': 2, 'd': 3}
dictB = {'a': 0, 'c': 3, 'd': 3}

def main():
    # Using loop
    common = {}
    for key, value in dictA.items():
        if key in dictB:
            common[key] = value
    print(common)

    # Using a dictionary comprehension
    common = {key: value for key, value in dictA.items() if key in dictB}

main()