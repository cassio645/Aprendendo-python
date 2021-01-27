# Testando a velocidade de:   dict normal e defaultdict

from collections import defaultdict
from timeit import timeit

animais = [('gato', 1), ('coelho', 2), ('gato', 3), ('cachorro', 4), ('cachorro', 4)]

std_dict = {} # dicionario normal
def_dict = defaultdict(list)  # defaultdict q cria listas


def grupo_com_dict():
    for animal, cont in animais:
        std_dict.setdefault(animal, []).append(cont)
    return std_dict

def grupo_com_defaultdict(): # menos confuso, acho
    for animal, cont in animais:
        def_dict[animal].append(cont)
    return def_dict


print(f'dict.setdefault() fez em {timeit(grupo_com_dict)} segundos.')
print(f'defaultdict fez em {timeit(grupo_com_defaultdict)} segundos.')
