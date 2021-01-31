# Transpor - Os indices de linha e coluna são trocados
import numpy as np

a = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
])

print(a.T)
# ou
print(a.transpose())
print('-'*40)



# Ordenando

dados = np.array([
                  [7, 1, 4],
                  [8, 6, 5],
                  [1, 2, 3]
])

np.sort(dados) # Ordena as linhas
np.sort(dados, axis=None) # faz tudo ficar na mesma linha ordenado
np.sort(dados, axis=1) # Orena tudo certinho, cada um em sua linha
print('-'*50)



# Concatenando


c = np.array([
              [4, 8],
              [6, 1]
])

b = np.array([
              [3, 5],
              [7, 2]
])
print(np.hstack((c, b))) # Junta os dois arrays, respeitando as linhas dos mesmos
print(np.vstack((c,b))) # Junta os dois arrays, porem colocando um embaixo do outro verticalmente
print('-'*40)
np.concatenate((c,b)) # Faz o mesmo do vstack
np.concatenate((c,b), axis=None) # concatena tudo em uma linha
