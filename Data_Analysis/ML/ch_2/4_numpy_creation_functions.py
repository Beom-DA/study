import numpy as np


##### arange
a = np.arange(30)

np.arange(30).reshape(-1,5)
np.arange(0, 5, 0.5)


##### ones, zeros & empty
np.zeros(shape=(10,), dtype=np.int8) # 10 - zero vector 생성
np.zeros((2,5)) # 2 by 5 - zero matrix 생성
np.ones(shape=(10,), dtype=np.int8) 
np.ones((2,5))
np.empty(shape=(10,), dtype=np.int8) # empty는 잘 안씀
np.empty((3,5))

test_matrix = np.arange(30).reshape(5,6)
np.zeros_like(test_matrix)

##### something_like
test_matrix = np.arange(30).reshape(-1,6)
a = np.ones_like(test_matrix)
#print(a)


##### eye, identity & digonal
np.identity(n=3, dtype=np.int8)
np.identity(5)

np.eye(N=3, M=5, dtype=np.int8)
np.eye(3)
np.eye(3,5,k=2) # k --> start index

matrix = np.arange(9).reshape(3,3)
np.diag(matrix)
np.diag(matrix, k=1)

np.random.uniform(0,1,10).reshape(2,5)
np.random.normal(0,1,10).reshape(2,5)