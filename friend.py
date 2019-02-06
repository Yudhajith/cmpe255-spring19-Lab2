import numpy as np

def mean_num_friends(x):
    return np.mean(x)

def median_num_friends(x):
    return np.median(x)

num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]
print("Mean = ", mean_num_friends(num_friends))
print("Median = ", median_num_friends(num_friends))