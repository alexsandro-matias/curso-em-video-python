# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

import random

# import time

quantidade_palpites = 0

numeroComputador = random.randint(0, 10)
numeroJogador = int(input('Digite o número inteiro entre 0 e 10: '))
quantidade_palpites = quantidade_palpites + 1

while numeroJogador != numeroComputador:
    print('Seu número: {} é diferente do selecionado do computador. '.format(numeroJogador))
    numeroJogador = int(input('Digite outro número: '))
    quantidade_palpites = quantidade_palpites + 1
    # print('PROCESSANDO')
    # time.sleep(3)

if numeroComputador == numeroJogador:
    print('Parabéns, você acertou o número da máquina')
    print("Quantidade de palpites: {}.".format(quantidade_palpites))
