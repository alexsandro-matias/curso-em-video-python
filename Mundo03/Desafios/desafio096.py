

desafio 096
faça um programa que tenha uma função chamada area(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


controle de Terrenos
_____________________

largura (m): 4.5
comprimento (m): 8
A área de um terreno 4.5 X 8.0 é de 36.0 m².

def area_terreno(largura, comprimento):
    print(f'A área de um terreno {largura} m X {comprimento} m é de {largura * comprimento} m²')

largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento(m): '))
area_terreno(largura, comprimento)


desafio 097
Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com o tamanho adaptável:

Ex:
escreva ('Olá, Mundo')

Saída:
_________
Olá mundo
__________


def escreva(mensagem):
    quantidade_caracteres = len(mensagem)
    print('~' * quantidade_caracteres)
    print(mensagem)
    print('~' * quantidade_caracteres)

texto = input('Digite o texto: ')

escreva(texto)



Falta corrigir

# desafio 098
# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo e realiza a contagem.
#
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
#

def contagem(inicio , fim , passo = 1):

    if inicio <= fim:
        for i in range(inicio, fim+1, passo):
            print(i)
    else:
        for i in range(fim, inicio, passo):
            print(i)

# contagem(10,50,5)
contagem(10,0,2)
# contagem(10,50,5)





desafio 099
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(numeros):
    lista = list(numeros)
    maior_numero = lista[0]

    for i in lista:
        if i > maior_numero:
            maior_numero = i

    print(maior_numero)

valores = [10, 1 , 11 , 7 , 8 , 9]
maior(valores)







desafio 100
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e soma_par().
A primeira função vai sortear
5 números e vai colocá-los dentro da lista
e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

numeros = []

from random import randint

def sorteia():
    for i in range(5):
        numeros.append(randint(0,100))

def soma_par():
    sorteia()
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print(f' Os números sorteados {numeros} e a soma dos pares - {soma}')


soma_par()
