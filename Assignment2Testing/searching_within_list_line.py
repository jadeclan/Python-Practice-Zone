my_list = ["apple", "banana", "cherry", "banana"]
find_item ='pp'

# Method 1: Using index() to find the first occurrence doesn't work for substrings
try:
    index = my_list.index(find_item)
    print(f"The first {find_item} is at index: {index}")
except ValueError:
    print(f"{find_item} not found in the list.")

# Method 2: Using a loop to find the first occurrence of a substring works
for i, item in enumerate(my_list):
    if find_item in item:
        print(f"Found {find_item} at index: {i}")
        break
    else:
        print(f"{find_item} not found in item: {item}")