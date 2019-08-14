# Desenvolva um programa que leia as duas notas de aluno,
# e calcule e mostre sua média

primeiraNota = float(input('Digite a primeira nota do aluno: '))
segundaNota = float(input('Digite a sua segunda nota: '))
media = (primeiraNota + segundaNota)/2
print('A média do aluno foi: {:.2f}'.format(media))