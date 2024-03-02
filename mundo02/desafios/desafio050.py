# Desafio 50
# Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o

soma = 0

for i in range (1,7):
    numero = int(input('Digite o {}º número: '.format(i)))
    if (numero % 2 == 0):
        soma = soma + numero

print('A soma dos número pares digitados foi: {}.'.format(soma))