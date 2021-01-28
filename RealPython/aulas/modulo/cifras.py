import string

def cifra_cesar(msg, cod, decifra=False):
    if not msg.isascii() or not msg.isalpha():
        raise ValueError('Texto invalido. Não use caracteres especiais, ou números')

    lowercase = string.ascii_lowercase # aqui esta todo alfabeto em minusculo
    uppercase = string.ascii_uppercase # em maiusculo
    resultado = ''

    if decifra:
        cod = cod * -1

    for letra in msg:
        if letra.islower():
            i = lowercase.index(letra)
            resultado += lowercase[(i + cod) % 26]
        else:
            i = uppercase.index(letra)
            resultado += uppercase[(i + cod) % 26]

    return resultado


txt = 'assimquefazcifra' # não pode conter espaços 
texto_cesar = cifra_cesar(txt, 5) # adicione  True como argumento caso queira fazer o inverso(traduzir)
print(texto_cesar)
