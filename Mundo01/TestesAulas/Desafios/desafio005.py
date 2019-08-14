# Faça um programa que leia um número inteiro
# e mostre seu sucessor e seu antecessor

numero = int(input('Digite um número inteiro: '))
print('{} tem como antecessor {} e sucessor {}'.format(numero , numero-1, numero+1))