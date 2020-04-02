# Desafio 018
# Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import sin,cos,tan,radians
angulo = float(input('Digite o valor do ângulo em º: '))
angulo = radians(angulo)
print('Seno: {:.2f}'.format(sin(angulo)))
print('Cosseno: {:.2f}'.format(cos(angulo)))
print('Tangente: {:.2f}'.format(tan(angulo)))
