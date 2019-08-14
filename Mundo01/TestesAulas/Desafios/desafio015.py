# Escreva um programa que pergunte a quantidade de KM percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar,
# sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por KM rodado.

quantidadeDias = int(input('Informe a quantidade de dias que o carro passou alugado: '))
kilometragem = float(input('Informe quantos KM foram percorridos pelo carro: '))
valor = 60 * quantidadeDias + kilometragem * 0.15
print('O valor total é de R${:.2f}'.format(valor))