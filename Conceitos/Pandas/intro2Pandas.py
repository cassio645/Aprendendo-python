import pandas as pd

alunos = {
    'Nome': ['Ricardo', 'Pedro', 'Maria', 'Bianca', 'Maria', 'Ana'],
    'Nota': [6, 8, 9, 4.2, 5, 7],
    'Aprovado': ['Sim', 'Sim', 'Sim', 'Não', 'Não', 'Sim']
}
alunosFrame = pd.DataFrame(alunos)

# Filtrando dados
# colunas
print(alunosFrame['Nome'])

# linhas
print(alunosFrame.loc[[5]]) # imprime a linha com aquele indice
print(alunosFrame.loc[1:4]) # metodo de fatiamento igual das listas

print('-'*30)

# Filtrando com dados em vez de indices
print(alunosFrame.loc[alunosFrame['Nome'] == 'Maria']) # a busca é por valores
print('-'*30)
print(alunosFrame.loc[alunosFrame['Nota'] > 7])
print('-'*30)
print(alunosFrame.loc[alunosFrame['Aprovado'] == 'Não'])
