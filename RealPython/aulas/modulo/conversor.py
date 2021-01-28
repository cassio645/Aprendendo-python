# conversor de minutos em dias
'''
def converte_minutos_em_dias(total_min):
    dias = total_min // 1440 # Sabendo q:  1 Dia == 1440 min
    resto = total_min % 1440

    horas = resto // 60
    minutos = resto % 60

    print(f'{total_min} min = {dias}d, {horas}h, e {minutos} min')
'''


# Usando divmod
def converte_minutos_em_dias(total_min):
    dias, resto = divmod(total_min, 1440) # Sabendo q:  1 Dia == 1440 min
    horas, minutos = divmod(resto, 60) #divmod retorna primento // depois % de (x,y)

    print(f'{total_min} min = {dias}d, {horas}h, e {minutos} min')

converte_minutos_em_dias(1503)
converte_minutos_em_dias(1000)
converte_minutos_em_dias(3456)
converte_minutos_em_dias(35000)