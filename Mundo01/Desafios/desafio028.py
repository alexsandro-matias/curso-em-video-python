# Desafio 028
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuuário tentar descobrir qual o npumero escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu
import random
import time

numeroComputador = random.randint(0,5)
numeroJogador = int(input('Digite o número inteiro entre 0 e 5: '))
print('PROCESSANDO')
time.sleep(3)
print('Seu número: {}. '.format(numeroJogador))
print('Número do computador: {}'.format(numeroComputador))
if numeroComputador == numeroJogador:
    print('Parabéns, você ganhou!!!')
else:
    print('Foi triste! Você perdeu!')




