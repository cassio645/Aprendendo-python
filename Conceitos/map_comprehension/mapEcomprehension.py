# Convertendo lista km para milhas
kmH = [40, 50, 56, 64, 73, 85, 96, 42, 120]


milhas = []
for x in kmH:
    milhas.append(x/1.61)
print(milhas)


# MAP - função map aplica um conjunto de dados a uma função
milhas2 = list(map(lambda x: x/1.61,kmH))
print(milhas2)


# COMPREHENSION
milhas3 = [x/1.61 for x in kmH]
print(milhas3)

caracteres = [i.upper() for i in 'Uma frase random']
print(caracteres)