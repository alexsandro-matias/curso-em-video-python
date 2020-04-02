# Crie um programa que leia quanto dinheiro um pesso tem na carteira
# mostre quantos dólares ela pode comprar
# US$ 1 = 3.27

reais = float(input('Quantos R$ você tem: '))
dolares = reais / 3.27
print('Você pode comprar US${:.2f}'.format(dolares))