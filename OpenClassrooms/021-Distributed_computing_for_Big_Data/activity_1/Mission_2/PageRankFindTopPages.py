import numpy as np

# Define number of top results to return
top_n = 20

M = np.loadtxt('results.txt')

top_idx = np.argsort(M[:, 1])[::-1][:top_n]
print(M[top_idx, :])