# Desafio 038
# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior;
# - O segundo valor é maior;
# - Não existe valor maior, os dois valores são iguais.


primeiro  = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))

if primeiro >  segundo:
    print('O primeiro valor é maior')

elif segundo > primeiro:
    print('O segundo valor é maior')

else:
    print('Não existe valor maior, os dois valores são iguais.')
