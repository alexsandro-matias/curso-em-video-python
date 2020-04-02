# Desafio 024
# Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome "santo"

nomeCidade = input('Digite o nome completo da cidade: ')
nomeCidade = nomeCidade.lower()
primeiroNome = nomeCidade.split()
print('santo' in primeiroNome[0])