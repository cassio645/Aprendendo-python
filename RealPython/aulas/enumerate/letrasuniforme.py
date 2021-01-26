'''def even_items(iteravel):
    valores = []
    for idx, valor in enumerate(iteravel, start=1):
        if not idx % 2:
            valores.append(valor)
    return valores'''

def even_items(iteravel):
    return[valor for i, valor in enumerate(iteravel, start=1) if not i % 2]

# Função geradora
def alfabeto():
    todas_letras = "abcdefghijklmnopqrstuvwxyz"
    for letra in todas_letras:
        yield letra


letras = alfabeto()
resposta = even_items(letras)
print(resposta)

#alfabeto = "abcdefghijklmnopqrstuvwxyz"
#print(list(alfabeto[1: :2]))
