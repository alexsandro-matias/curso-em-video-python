# Desafio 51
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = int(input('Digite o primeiro termo da Progressão Aritmética: '))
razao = int(input('Digite a razão (constante) dessa Progressão: '))

for numero in range(primeiro_termo,12):
    print(primeiro_termo, end=' ')
    primeiro_termo = primeiro_termo + razao
