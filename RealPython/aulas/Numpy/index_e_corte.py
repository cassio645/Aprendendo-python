import numpy as np

a = np.array([
    [0, 1, 2, 3, 4, 5],
    [10, 11, 12, 13, 14, 15],
    [20, 21, 22, 23, 24, 25],
    [30, 31, 32, 33, 34, 35],
    [40, 41, 42, 43, 44, 45],
    [50, 51, 52, 53, 54, 55],
])

print(a)

laranja = a[0, 3:5]
vermelho = a[: , 2]
verde = a[2::2, ::2] 
ciano = a[4: , 4:]

print('--LARANJA --')
print(laranja) # [3,4]
print('--VERMELHO---')
print(vermelho) # [2,12, 22, 32, 42, 52]
print('--VERDE---')
print(verde) # [20, 22, 24, 40, 42, 44]
print('--CIANO---')
print(ciano) # [44, 45, 54, 55]
print('-----')