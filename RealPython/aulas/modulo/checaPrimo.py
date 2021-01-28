def checa_primo(num):
    if num < 2:
        return f'Para ser um número primo ele deve ser maior ou igual a 2'
    
    cont = [(1, num)]
    i = 2

    while i * i <= num:
        if num % i == 0:
            cont.append((i, num//i))
        i += 1
    
    if len(cont) > 1:
        return f'{num} Não é primo pois ele foi divisivel por {cont}'
    else:
        return f'{num} É primo pois ele só é divisivel por 1 e por ele mesmo.'

print(checa_primo(5))
print(checa_primo(15))
print(checa_primo(1))
print(checa_primo(22))
