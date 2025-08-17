import numpy as np


def n_size_ndarray_creation(n, dtype=int):
    X = np.arange(n**2, dtype=int).reshape(n,n)
    return X

#print(n_size_ndarray_creation(3))














def zero_or_one_or_empty_ndarray(shape, type=0, dtype=int):
    if type == 0:
        X = np.zeros(shape, dtype=int)
    else:
        X = np.ones(shape, dtype=int)
    return X


#print(zero_or_one_or_empty_ndarray(shape=(2,2), type=1))


















def change_shape_of_ndarray(X, n_row):
    if n_row == 1 :
        return X.reshape(n_row,-1).flatten()
    return X.reshape(n_row,-1)
# X = np.ones((32,32), dtype=int)
# print(change_shape_of_ndarray(X, 512))












def concat_ndarray(X_1, X_2, axis):
    if len(X_1.shape) == 1 :
        X_1 = X_1.reshape(1,X_1.shape[0])
    if len(X_2.shape) == 1 :
        X_2 = X_2.reshape(1,X_2.shape[0])
    if axis == 0 :
        if X_1.shape[1] == X_2.shape[1] :
            return np.concatenate((X_1,X_2), axis=0)
        else:
            return False
    else :
        if X_1.shape[0] == X_2.shape[0] :
            return np.concatenate((X_1,X_2), axis=1)
        else :
            return False


# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6]])
# print(concat_ndarray(a, b, 0))
# print(concat_ndarray(a, b, 1))
# a = np.array([1, 2])
# b = np.array([5, 6, 7])
# print(concat_ndarray(a, b, 1))
# print(concat_ndarray(a, b, 0))









def normalize_ndarray(X, axis=99, dtype=np.float32):
    if axis == 0:
        row_mean = X.mean(axis=0, keepdims = True)
        row_std = X.std(axis=0, keepdims = True)
        return (X-row_mean) / row_std
    elif axis == 1:
        col_mean = X.mean(axis=1, keepdims = True)
        col_std = X.std(axis=1, keepdims = True)
        return (X-col_mean) / col_std
        return 
    else :
        return (X-X.mean()) / X.std()

# X = np.arange(12, dtype=np.float32).reshape(6,2)
# print(normalize_ndarray(X))
# print(normalize_ndarray(X, 1))
# print(normalize_ndarray(X, 0))














def save_ndarray(X, filename="test.npy"):
    np.save(filename, X)
    return True

X = np.arange(32, dtype=np.float32).reshape(4, -1)
filename = "test.npy"
#print(save_ndarray(X, filename)) #test.npy 파일이 생성됨












def boolean_index(X, condition):
    return X[eval(str('X') + condition)]

# X = np.arange(32, dtype=np.float32).reshape(4, -1)
# print(boolean_index(X, "== 3"))
# X = np.arange(32, dtype=np.float32)
# print(boolean_index(X, "> 6"))













def find_nearest_value(X, target_value):
    arr = np.full((len(X),), target_value)
    diff = abs(X-arr)
    index = np.where(diff == diff.min()) 
    return X[index]

# X = np.random.uniform(0, 1, 100)
# target_value = 0.3
# print(find_nearest_value(X, target_value)) # 출력되는 값은 random 하게 바뀜









def get_n_largest_values(X, n):
    X = np.sort(X)[::-1]
    return X[:n]

X = np.random.uniform(0, 1, 100)
print(get_n_largest_values(X, 3))
print(get_n_largest_values(X, 5))
# 출력되는 값은 random 하게 바뀜