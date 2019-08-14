# Desafio 031
# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando
# R$ 0,50 por Km para viagens até 200 Km e R$ 0,45 para viagens mais longas.
distancia = float(input('Digite a distância da viagem em Km: '))
if distancia >= 200:
    passagem = distancia * .45
else:
    passagem = distancia * .5
print('O valor da passagem é: R$ {:.2f}'.format(passagem))