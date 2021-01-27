from collections import defaultdict

dep = [('Vendas', 'John Doe'),
       ('Vendas', 'Martin Smith'),
       ('Contabilidade', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe')]

''' # Com list
dep_dicio = defaultdict(list)
for departamento, empregado in dep:
    dep_dicio[departamento].append(empregado)
# Cria chaves com nome dos departamentos, e adiciona numa lista os empregados
# daquele departamento
print(dep_dicio)
'''


'''
# Com set
dep_dicio = {}
for departamento, empregado in dep:
    dep_dicio.setdefault(departamento, []).append(empregado)
# Aqui cria uma chave com departamento, cria uma lista vazia e ja a preenche
# com o empregado
print(dep_dicio)
'''
print('-'*90)



'''
# Trabalhando com itens duplicados no banco de dados
depart = [('Vendas', 'John Doe'),
                ('Vendas', 'Martin Smith'),
                ('Contabilidade', 'Jane Doe'),
                ('Marketing', 'Elizabeth Smith'),
                ('Marketing', 'Elizabeth Smith'),
                ('Marketing', 'Adam Doe'),
                ('Marketing', 'Adam Doe'),
                ('Marketing', 'Adam Doe')]

dep_dicio = defaultdict(set)
for departamento, empregado in depart:
    dep_dicio[departamento].add(empregado)
print(dep_dicio)
# Vai corrigir o erro, nao adicionando o mesmo empregado 2x
'''



# Contando número de funcionarios por departamento
dicio = defaultdict(int)
for departamento, emp in dep:
    dicio[departamento] += 1
# defaultdict(<class 'int'>, {'Vendas': 2, 'Contabilidade': 1, 'Marketing': 2})
print(dicio)