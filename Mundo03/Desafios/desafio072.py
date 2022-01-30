# desafio 072
# Crie um programa que tenha uma
# tupla totalmente preenchida com uma contagem por extenso de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20)

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero = int(input('Digite um número entre 0 e 20: '))

while numero < 0 or numero > 20:
    print('Número Digitado fora da faixa.')
    numero = int(input('Digite um número entre 0 e 20: '))

print("O número digitado foi {}.".format(numeros[numero]))
