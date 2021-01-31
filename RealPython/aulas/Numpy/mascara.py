import numpy as np
from numpy.random import default_rng

# Cria um array do 5 ao 50 com 24 itens     com 4 linhas
numeros = np.linspace(5, 50, 24, dtype=int).reshape(4, -1)
print(numeros)

mascara = numeros % 4 == 0
# array onde todos divisiveis por 4 vao ter True
print(mascara)

print('-'*30)
print(numeros[mascara]) # mostra os num divisiveis

# outra forma filtrando
div4 = numeros[numeros % 4 == 0]
print(div4)

print('\n', '-'*90, '\n')

rng = default_rng()
valores = rng.standard_normal(10000)
print(valores[:5])

std = valores.std()
print(std)

filtrado = valores[(valores > -2 * std) & (valores < 2 * std)]
print(filtrado.size)
print(valores.size)
print(filtrado.size/ valores.size)