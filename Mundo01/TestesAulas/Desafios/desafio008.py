# Escreva um programa que leia o valor em metros
# e exiba convertido em centrímetros e melímetros
metros = float(input('Digite um valor em metros: '))
print('O valor digitado equivale a {} cm e {} mm.'.format(metros*100, metros*1000))