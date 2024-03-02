# Desafio 52
# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.

numero = int(input('Digite um número: '))
contador = 0

for i in range(1,numero+1):
    if numero % i == 0 :
        contador = contador + 1

if contador == 2:
    print('O número {} é primo: '.format(numero))
else:
    print('O número {} não é primo.'.format(numero))

