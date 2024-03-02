# Desafio 54
# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
# Maioridade 21 anos

from datetime import date

maiores = 0
menores = 0

for i in range(1, 8):
    ano_nascimento = int(input('Digite a idade da {}ª pessoa: '.format(i)))
    idade = date.today().year - ano_nascimento
    if idade >= 18:
        maiores = maiores + 1
    else:
        menores = menores + 1

print('Quantidade de pessoas maiores de idade: {}.'.format(maiores))
print('Quantidade de pessoas menores de idade: {}.'.format(menores))
