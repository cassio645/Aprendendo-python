a_dicio = {'a': 1} 
# Caso b ja exista exemplo {'a': 1, 'b': 5} ele ignora os argumentos do get e do set(2)
# e retorna 5 o valor ja existente se existente

print(a_dicio.get('b', 2))
print(a_dicio)

print('-'*30)
print(a_dicio.setdefault('b', 2))
print(a_dicio)
print('-'*30)


# Usando condicionais para criar uma chave caso ela n exista
b_dicio = {}
if 'key' in b_dicio:
    print(b_dicio['key'])
else:
    b_dicio['key'] = 'Valor padrão'

print(b_dicio)
print('-'*30)

# Usando Try para criar um item caso nao exista
c_dicio = {}
try:
    print(c_dicio['key'])
except KeyError:
    c_dicio['key'] = 'valor padrão também'

print(c_dicio)