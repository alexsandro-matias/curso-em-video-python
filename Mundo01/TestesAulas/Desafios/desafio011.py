# Faça um programa que leia a largura e altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma ára de 2m²

altura = float(input('Digite a altura da parede: '))
comprimento = float(input('Digite o comprimento da parede: '))
area = altura * comprimento
print('A área da parede é de {}m² e serão necessários {} litros de tinta para pintá-la.'.format(area,area/2))
