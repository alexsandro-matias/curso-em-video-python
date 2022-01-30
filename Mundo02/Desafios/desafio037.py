# Desafio 037
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - Para binário;
# - Para Hexadecimal;
# - Para Octal.
#

numero = int(input('Digite um número inteiro: '))
binario = bin(numero)
hexadecimal = hex(numero)
print(hexadecimal)
