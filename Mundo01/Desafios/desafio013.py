# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.

salarioAntigo = float(input('Digite o salário atual: R$  '))
salarioNovo = salarioAntigo * 1.15
print('salário anterior: R$ {:.2f}'.format(salarioAntigo) , end=' >>>> ')
print('salário com aumento: R$ {:.2f}'.format(salarioNovo))