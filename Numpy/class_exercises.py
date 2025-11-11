
import numpy as np
# arr = np.array([1, -2, 3, 0, -4, 2])
# print(arr<0)
# arr[arr < 0] = 0
# print(arr)  # prints [1, 0, 3, 0, 0, 2]

# arr = np.array([1, -2, 3, 0, -4, 2])
# is_negative = arr < 0
# arr[is_negative] = 0
# print(arr)  # prints [1, 0, 3, 0,


# scores = np.array([
#     ['alice', 5],
#     ['bob', 3],
#     ['cindy', 4],
#     ['david', 1],
#     ['edith', 2]
# ])
# is_alice = scores[:, 0] == 'alice'
# is_david = scores[:, 0] == 'david'
# is_not_alice_or_david = ~ (is_alice | is_david)
# print(scores[is_not_alice_or_david])

# """Get the table slice(view) that excludes alice and david."""
# table_slice = scores[(scores[:, 0] != 'alice') & (scores[:, 0] != 'david')]
# print(table_slice)  # prints [['bob' '3'] ['cindy' '4'] ['edith' '2']]

coordinates = np.random.random((100, 2))
current_location = np.array([0.5, 0.5])
taxicab_distances = np.abs(coordinates - current_location).sum(axis=1)
print(coordinates, current_location)
print((taxicab_distances))

# add dx to dy
# or
taxicab_distances = np.abs(coordinates - current_location).sum(axis=1)
# find index of smallest distance
indx = taxicab_distances.argmin()
print(indx, taxicab_distances[indx])

test_range = np.arange(0,5)
print(test_range)
print('2:5', test_range[2:5])

