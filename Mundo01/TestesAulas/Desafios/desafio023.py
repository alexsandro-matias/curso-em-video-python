# Desafio 023
# Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos dígitos separados
#
# Ex: Digite o número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1


numero = int(input('Digite um número entre 0 e 9999: '))
unidade = numero % 10
numero = numero - unidade
numero = numero / 10

dezena = numero % 10
numero = numero - dezena
numero = numero / 10

centena = numero % 10
numero = numero - centena
numero = numero / 10

milhar = numero % 10
numero = numero - milhar

print('Milhar: {:.0f}'.format(milhar))
print('Centena: {:.0f}'.format(centena))
print('Dezena: {:.0f}'.format(dezena))
print('Unidade: {}'.format(unidade))



