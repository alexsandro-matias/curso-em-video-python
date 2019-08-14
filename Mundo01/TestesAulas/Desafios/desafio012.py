# Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço com 5%¨de desconto.
valorAntigo = float(input('Digite o preço atual do produto: R$  '))
valorNovo = valorAntigo * 0.95
print('Valor anterior: R$ {:.2f}'.format(valorAntigo) , end=' >>>> ')
print('Valor com desconto: R$ {:.2f}'.format(valorNovo))