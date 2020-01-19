import pandas as pd

import numpy as np

arr = np.arange(12).reshape((3,4))

print(arr)

d = np.arange(16).reshape(4,4)

s = np.concatenate([arr, d], axis = 0)

print(s)

s1 = pd.Series([0, 1], index = ['a', 'b'])
s2 = pd.Series([2, 3, 4], index = ['c', 'd', 'e'])
s3 = pd.Series([5, 6], index = ['f', 'g'])

a = pd.concat([s1, s2, s3], axis = 1)

s4 = pd.concat([s1, s3])

print(s4)

b = pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']])

print(b)

result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])

print(result)
