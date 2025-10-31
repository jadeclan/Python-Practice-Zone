import numpy as np

# maxi = 0
# mini = 0
# for i in range(1000000):
#     data = np.random.rand(2,3)*2 - 1  # Random values between -1 and 1
#     if np.max(data) > maxi:
#         maxi = np.max(data)
#     if np.min(data) < mini:
#         mini = np.min(data)

# print(mini, maxi)

arr = np.arange(5)
print(np.exp(arr))  # e^x where x is each element in the array