import numpy as np

test_array = np.array(['1','4', 5, 8], float)
# print(test_array)
# print(type(test_array[3]))
# print(test_array.shape)
# print(test_array.dtype)


tensor  = [[[1,2,5,8],[1,2,5,8],[1,2,5,8]], 
           [[1,2,5,8],[1,2,5,8],[1,2,5,8]], 
           [[1,2,5,8],[1,2,5,8],[1,2,5,8]], 
           [[1,2,5,8],[1,2,5,8],[1,2,5,8]]]
# print(np.array(tensor, int).shape)
# print(np.array(tensor, int).ndim)
# print(np.array(tensor, int).size)


a = np.array([[1, 2, 3], [4.5, 5, 6]], dtype=int)
b = np.array([[1, 2, 3], [4.5, "5", "6"]], dtype=np.float32)
c = np.array([[1, 2, 3], [4.5, "5", "6"]], dtype=np.float32).nbytes