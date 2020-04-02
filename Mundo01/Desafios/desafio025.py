# Desafio 025
# Crie um programa que leia o nome de uma pessoa
# e diga se ela tem "silva" no nome
nome = input('Digite o nome completo da pessoa: ')
nomeMinusculo = nome.lower()
print('Ela possue "Silva" no nome: {}'.format('silva' in nomeMinusculo))