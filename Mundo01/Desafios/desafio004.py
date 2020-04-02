# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

a = input(('Digite qualquer coisa:'))
print(type(a))
print(a.isnumeric())
print(a.islower())
print(a.isupper())
print(a.isalnum())
print(a.isalpha())