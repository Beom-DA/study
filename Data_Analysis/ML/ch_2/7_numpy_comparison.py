import numpy as np

a = np.arange(10)
print(a>5)
print(np.any(a>5), np.any(a<0))
print(np.all(a>5) , np.all(a < 10))


##### comparision operation
test_a = np.array([1, 3, 0], float)
test_b = np.array([5, 2, 1], float)
print(test_a > test_b) 


##### np.where
a = np.array([1, 3, 0], float)
print(np.where(a > 0, 3, 2)) # a의 각 인덱스의 값이 0보다 크면 3을, 0보다 작거나 같으면 2를 반환
# 결과값 : [3 3 2]
np.where(a>0) # True면 index값을 반환, False면 아무것도 반환안함
a = np.arange(5, 15)
np.where(a>10)


##### argmax & argmin
a = np.array([1,2,4,5,8,78,23,3])
np.argmax(a) , np.argmin(a) # index를 반환

a=np.array([[1,2,4,7],[9,88,6,45],[9,76,3,4]])
np.argmax(a, axis=1) , np.argmin(a, axis=0) #index를 반환






































