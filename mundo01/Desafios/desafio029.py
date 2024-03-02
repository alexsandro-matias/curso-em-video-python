# Desafio 029
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 para cada Km acima do limite.
velocidade = float(input('Informe a velocidade do veículo: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('O valor da multa a pagar: {:.2f}'.format(multa))
else:
    print('Suave na nave! Se manda!')