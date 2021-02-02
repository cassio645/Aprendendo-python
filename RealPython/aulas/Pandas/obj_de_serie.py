import pandas as pd

# Como uma lista
dados = pd.Series([5555, 7000, 1980])
print(dados.values)
print(dados.index)
print('-'*30)

# Atribuindo indices de palavras
dados_receita = pd.Series(
    [4200, 8000, 6500],
    index=['Amsterdam', 'Toronto', 'Tokyo']
)
print(dados_receita)
print('-'*30)

# Construindo igual um dicionario
dados_funcionario = pd.Series(
    {'Amsterdam': 5, 'Tokyo': 8}
)
print(dados_funcionario)
print(dados_funcionario.keys())
print('New York' in dados_funcionario)
print('-'*60)

# Construindo um dataframe com os dados acima

cidade = pd.DataFrame({
    'Receita': dados_receita,
    'Funcionarios': dados_funcionario 

})
print(cidade)
print(cidade.index)
print('-'*20)
print(cidade.values)
print('-'*60)

# ------ Acessando elementos -------
print(dados_receita['Toronto']) # or dados_receita[1]
print(dados_receita['Toronto':]) # or dados_receita[1:]