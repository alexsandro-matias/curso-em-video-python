# Desafio 56
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final mostre:
#
# A média de idade do grupo.
# Qual é o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos.

quantidade_pessoas = 2
soma_idades = 0
idade_mais_velho = 0
nome_mais_velho = ''

media_idade = 1
quantidade_mulheres_20 = 0

for i in range(quantidade_pessoas):
    nome = input(f'Qual o nome da {i + 1}ª pessoa: ')
    sexo = input('Informe seu sexo: ')
    idade = int(input('Informe sua idade: '))

    if idade > idade_mais_velho:
        nome_mais_velho = nome

    if sexo == 'f' or sexo == 'F' and idade > 20:
        quantidade_mulheres_20 = + 1

    soma_idades = soma_idades + idade

media_idade = soma_idades / quantidade_pessoas

print(f'A média de idade do grupo: {media_idade}')
print(f'O nome do mais velho: {nome_mais_velho}')
print(f'Quantidade de mulheres mais velhas: {quantidade_mulheres_20}')
