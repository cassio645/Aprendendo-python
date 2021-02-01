import pandas as pd

'''
dados = pd.read_excel('C:/Users/CASSIO/Documents/Python/Aprendendo-python/Conceitos/pandas/arquivo1.xlsx')
print(dados.head())
'''

dados2 = pd.read_csv('C:/Users/CASSIO/Documents/Python/Aprendendo-python/Conceitos/pandas/athlete_events.csv')
print(dados2.head(10))
print(dados2.shape) # (271116, 15)
