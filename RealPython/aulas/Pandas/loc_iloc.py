import pandas as pd

cores = pd.Series(
    ['Red', 'Purple', 'Blue', 'Green', 'Yellow'],
    index=[1, 2, 3, 5, 8] # == 1: "Red"...
)

print(cores)
print(cores.iloc[1]) # refere-se ao indice   -  Purple
print(cores.loc[1]) # refere-se a posição na lista  - Red

# Fatiamento com iloc e loc
print(cores.iloc[1:3]) 
print(cores.loc[1:3]) # Inclui o elemento de fechamento tb

# indice negativo
print(cores.iloc[-2]) # Green  
# loc Não funciona com indice negativo

# iloc usado como em listas
#loc usado como em dicionarios