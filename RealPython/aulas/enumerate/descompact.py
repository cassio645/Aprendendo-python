tupla = (10, 'oi')
primeiro, segundo = tupla
print(primeiro)
print(segundo)

valores = ['a', 'b']
teste = enumerate(valores)
print(teste)
try:
    print(next(teste))
    print(next(teste))
    print(next(teste))
except StopIteration:
    print('fim dos valores')

print('-'*30)
# zip permite iterar as tres listas ao mesmo tempo, mais o enumerate indice
inicio = ['a', 'b', 'c']
meio = ['d', 'e', 'f']
fim = ['g', 'h', 'i']
for i, (um, dois, tres) in enumerate(zip(inicio, meio, fim)):
    print(i, um, dois, tres)
