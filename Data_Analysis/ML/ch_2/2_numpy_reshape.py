import numpy as np

test_matrix = [[1,2,3,4], [1,2,5,8]]
np.array(test_matrix).shape
np.array(test_matrix).reshape(2,2,2)

a = np.array(test_matrix).reshape(-1,2).shape
print(a)

test_matrix = [[[1,2,3,4], [1,2,5,8]], [[1,2,3,4], [1,2,5,8]]]
b = np.array(test_matrix).flatten()
print(b)