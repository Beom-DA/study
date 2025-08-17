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

print(zero_or_one_or_empty_ndarray(shape=(2,2), type=1))


def change_shape_of_ndarray(X, n_row):
    pass


def concat_ndarray(X_1, X_2, axis):
    pass


def normalize_ndarray(X, axis=99, dtype=np.float32):
    pass


def save_ndarray(X, filename="test.npy"):
    pass


def boolean_index(X, condition):
    pass


def find_nearest_value(X, target_value):
    pass


def get_n_largest_values(X, n):
    pass