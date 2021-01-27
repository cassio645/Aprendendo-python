from collections import defaultdict

print(issubclass(defaultdict, dict)) # True


# Quando pedir um valor q nao exista no disc ele cria uma lista vazia
# Porem pode ser um  int, str, float, não só lista
dicionario = defaultdict(list) 
print(type(dicionario))

dicionario['um'] = 1 # Normal dos dicionarios aqui
print(dicionario)

dicionario['novoitem'] # cria lista vazia para key 'novoitem'
print(dicionario['outroitem'].append(4))
# defaultdict(<class 'list'>, {'um': 1, 'novoitem': [], 'outroitem': [4]})
print(dicionario) 
