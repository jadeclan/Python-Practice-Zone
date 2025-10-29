import numpy as np

data1 = np.array([1, 2, 3, 4])  # a 1-D array (vector)
data2 = np.array([[1, 2], [3, 4]])  # a 2-D array
data3 = np.array([[1, 2, 3], [1,3, 4], [3,4,5]])  # a 2-D array

# print(data1.ndim, data1.shape)
# print(data2.ndim, data2.shape)
# print(data3.ndim, data2.shape)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[4, 3], [2, 1]])
#print(arr1 > arr2) # element wise comparison: is 1>4, is 2>3, is 3>2, is 4>1.

"""Create an array of 100 random numbers (between 0 and 1), like this:
   np.random.random(100). Scale the numbers between -1 and 1 (multiply by 2 and 
   subtract 1) Use vectorized operations for this. Get a running sum of the 
   numbers using the cumsum method
"""
random_numbers = np.random.random(100)
scaled_numbers = random_numbers * 2 - 1
running_sum = np.cumsum(scaled_numbers)
#print(running_sum)

"""Given these arrays of predicted outcomes and actual outcomes, compute the 
   mean-squared error. (i.e. error is predicted - actual, and mean-squared error 
   is the mean of the squares of all the errors)
"""
predicted = np.array([2, 4, 1, 6, 8, 4])
actual = np.array([4, 4, 0, 3, 7, 6])
squared_errors = (predicted - actual)**2
mean_squared_error = np.mean(squared_errors)
#print(f"Mean square error: {mean_squared_error:.2f}")

arr = np.array([0, 1, 2, 3, 4, 5])
arr[1:3] = 10
arr[3:5] = [100, 150]
#print(arr)

arr = np.array([0, 1, 2, 3, 4, 5])
slice = arr[2:5]
slice[0] = 999  # change a value in the slice
#print(arr)  # the original array is changed


"""Use np.ones to create a 3D array of ones with shape 5x6x7
   Access arr[0, :, :]. What shape do you expect it to be?
   Now access arr[1, :, 2:4]. What shape will it be?"""
arr = np.ones((5, 6, 7))
# print(arr[0, :, :].shape)    # Expected shape: (6, 7)
# print(arr[1, :, 2:4].shape)  # Expected shape: (6, 2)

arr = np.array([1, 2, 3, 4, 5, 6])
bigger_than_4 = arr > 4    # this is a boolean array
# print(arr[bigger_than_4])  # prints([5, 6]), where bigger_than_4 was true

scores = np.array([ ['alice', 5], ['bob', 3], ['cindy', 4] ])
bob_score = scores[scores[:, 0] == 'bob', 1]
# print(bob_score)  # prints [3]

"""Given an array, use boolean indexing to set all negative values to 0
"""
arr = np.array([1, -2, 3, 0, -4, 2])
arr[arr < 0] = 0
# print(arr)  # prints [1, 0, 3, 0, 0, 2]

"""Given a table of scores, get the names of everyone who scored between 2 and 
4 points. """
scores = np.array([
    ['alice', 5],
    ['bob', 3],
    ['cindy', 4],
    ['david', 1],
    ['edith', 2]
])
names_between_2_and_4 = scores[(scores[:, 1].astype(int) >= 2) & (scores[:, 1].astype(int) <= 4), 0]
# print(names_between_2_and_4)  # prints ['bob' 'cindy' 'edith']

"""Get the table slice(view) that excludes alice and david."""
table_slice = scores[(scores[:, 0] != 'alice') & (scores[:, 0] != 'david')]
# print(table_slice)  # prints [['bob' '3'] ['cindy' '4'] ['edith' '2']]

"""Create a set of 100 random x-y map coordinates.  Set our current location to
np.array([0.5, 0.5]). Compute the 100 taxicab distances from our current 
location to all the others. HINT1: you can subtract the 1x2 array from the 100x2
array (broadcasting). HINT2: the ndarray.sum method has an optional axis 
parameter indicating which axis to sum along. For example, .sum(axis=0) sums 
across rows, .sum(axis=1) sums across columns
"""
coordinates = [[.25, .75], [.3,.6]] #np.random.random((1, 2))
current_location = np.array([0.5, 0.5])
taxicab_distances = np.abs(coordinates - current_location).sum(axis=1)
# print(coordinates, current_location)
# print(taxicab_distances)


my_list = [1, 2.8, 3, 4, 5]
my_array = np.array(my_list)
my_array.shape
my_array.dtype
my_array.ndim
# print(my_array.shape, my_array.dtype, my_array.ndim)

# print(np.arange(0, 10, 2))

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(a.ndim)
# print(a.shape)
# print(len(a.shape) == a.ndim)# number of dimensions = number of elements in shape
# print(a.size) # a.size = total number of elements = product of elements in shape
# print(a.dtype)

x = np.ones(2, dtype=np.int64) #Puts two 64-bit integers (1's) in an array
# print(x)

np.linspace(0, 10, num=5) #Creates an array of 5 evenly spaced numbers between 0 and 10

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
print(np.concatenate((y, x), axis=None)) #Concatenates y as a new row to x

a=np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a.shape)
print(a[(a<4) | (a>7)]) #Prints elements of a that are less than 4 or greater than 7