#Desafio 016
# Crie um programa que leia um número real qualquer pelo teclado
# e mostre na tela a sua porção inteiro
from  math import trunc
numero = float(input('Digite um número real: '))
print('O número {} tem a sua parte inteira {}.'.format(numero, trunc(numero) ))

