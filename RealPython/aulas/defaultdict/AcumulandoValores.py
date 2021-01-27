# Calculando a receita total de cada produto
from collections import defaultdict

loja = [('Livros', 1250.00),
        ('Livros', 1300.00),
        ('Livros', 1420.00),
        ('Tutoriais', 560.00),
        ('Tutoriais', 630.00),
        ('Tutoriais', 750.00),
        ('Cursos', 2500.00),
        ('Cursos', 2430.00),
        ('Cursos', 2750.00),]

# calculando
total = defaultdict(float)
for produto, valor in loja:
    total[produto] += valor

# defaultdict(<class 'float'>, {'Livros': 3970.0, 'Tutoriais': 1940.0, 'Cursos': 7680.0}

for produto, valor in total.items(): # items aqui é palavra reservada do python
    print(f'Total para {produto}: R$ {valor:,.2f}')