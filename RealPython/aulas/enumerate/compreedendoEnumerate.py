def meu_enumerate(sequencia, start=0):
    n = start
    for item in sequencia:
        yield n, item
        n += 1

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro','Dezembro']

# Sem list ele retorna o lugar da memoria
ordenado = list(meu_enumerate(meses, start=1))

print(ordenado)
