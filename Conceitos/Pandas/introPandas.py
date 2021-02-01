import pandas as pd
import numpy as np

alunos = {
    'Nome': ['Ricardo', 'Pedro', 'Maria', 'Bianca', 'Carlos', 'Ana'],
    'Nota': [6, 5, 9, 4.2, 8, 7],
    'Aprovado': ['Sim', 'Não', 'Sim', 'Não', 'Sim', 'Sim']
}
alunosFrame = pd.DataFrame(alunos)
print(alunosFrame)
print('-'*40)

'''
obj1 = pd.Series([4, 5, 9, 10, 3])
print(obj1)
print('-'*40)

# passando um array para pd.Series SOMENTE ARRAYS UNIDIMENSIONAL 
a = np.array([15, 26, 84, 66, 12, 9])
obj2 = pd.Series(a)
print(obj2)
'''
print(alunosFrame.head(6))
print(alunosFrame.shape) # (6, 3) seis linhas  3 colunas
print(alunosFrame.describe()) # mt top
