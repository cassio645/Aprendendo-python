# Usando o operados % para criar uma iteração ciclica com Turtle
import turtle 
import random

def interacao_ciclica(t):
    cores = ['Green', 'Cyan', 'Orange', 'Purple', 'Red', 'Yellow', 'White']
    t.pendown()
    t.pencolor(random.choice(cores))

    i = 0
    while True:
        i = (i+1) % 6 # Mudando valor de i
        t.pensize(i) # o tamanho da caneta muda a cada iteracao
        t.forward(225)
        t.right(170)

        # A cada 6 iterações ele muda a cor
        if i == 0:
            t.pencolor(random.choice(cores))

wn = turtle.Screen()
wn.bgcolor('Gray8')
tarta = turtle.Turtle()
interacao_ciclica(tarta)