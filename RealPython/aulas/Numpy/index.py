import numpy as np

quadrado = np.array([
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1]
])

for i in range(4):
    assert quadrado[:, i].sum() == 34 
    assert quadrado[i, :].sum() == 34

assert quadrado[:2, :2].sum() == 34 # [16,3]   [5,10]

assert quadrado[2:, :2].sum() == 34 # [9,6]  [4,15]

assert quadrado[:2, 2:].sum() == 34 # [2,13]  [11,8]

assert quadrado[2:, 2:].sum() == 34 # [7, 12] [14,1]