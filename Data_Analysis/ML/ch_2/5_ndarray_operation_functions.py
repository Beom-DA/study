import numpy as np

test_array = np.arange(1,11)
test_array.sum(dtype=np.float)

test_array = np.arange(1,13).reshape(3,4)
test_array.sum()
test_array.sum(axis=1)
test_array.sum(axis=0)


third_order_tensor = np.array([test_array,test_array,test_array])
third_order_tensor.sum(axis=2)
third_order_tensor.sum(axis=1)


##### concatenate
a = np.array([[1, 2, 3]])
b = np.array([[2, 3, 4]])
np.concatenate( (a,b) ,axis=0)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
np.concatenate( (a,b.T) ,axis=1)

a.tolist()














































