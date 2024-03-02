# Desafio 034
# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salário superiores a R$ 1250,
# Calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%
#

salario = float(input('Digite o salário do funcionario: '))

if salario <= 1250:
    salario = salario * 1.15
else:
    salario = salario * 1.1

print('O salário do funcionário depois do aumento vai ficar: R$ {}'.format(salario))
