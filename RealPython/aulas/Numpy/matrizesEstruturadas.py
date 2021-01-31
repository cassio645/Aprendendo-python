import numpy as np
# Semelhante a banco de dados
dados = np.array([
                  ('joe', 32, 6),
                  ('mary', 15, 20),
                  ('felipe', 80, 100),
                  ('maria', 38, 9001),
], dtype=[('nome', str, 10), ('idade', int), ('power', int)])

print(dados[0])
print(dados['nome'])

print(dados[dados['power'] > 9000]['nome'])

'''
Exemplo SQL:
SELECT nome FROM dados
WHERE power > 9000
'''
print(np.sort(dados[dados['idade'] > 20], order='power')['nome'])