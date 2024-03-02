
# desafio 097
# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com o tamanho adaptável:

# Ex:
# escreva('Olá, Mundo')

# Saída:
# _________
# Olá mundo
# __________


def escreva(mensagem):
    quantidade_caracteres = len(mensagem)
    print('~' * quantidade_caracteres)
    print(mensagem)
    print('~' * quantidade_caracteres)


texto = input('Digite o texto: ')

escreva(texto)
