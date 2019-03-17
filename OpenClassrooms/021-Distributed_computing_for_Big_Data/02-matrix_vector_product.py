# Problem: Given a matrix A and a vector v,
# return the matrix-vector product A*v

import numpy as np

A = np.random.randn(5, 5)
v = np.random.randn(5, 1)


def map_function1(i, j, value):
    return((i, value * v[j]))

def reduce_function1(key, values):
    reduce_result = 0
    for val in values:
        reduce_result += val
    return(reduce_result)


# There are some subtilities when v does not fit entirely in MAP nodes memory
