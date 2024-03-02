# Desafio 033
# Faça um programa que leia três números e mostre qual é o maior e qual o menor
#

primeiro = int(input('Digite o primeiro número: '))
maior = primeiro
menor = primeiro

segundo = int(input('Digite o segundo número: '))
if segundo > maior:
    maior = segundo

if segundo < menor:
    menor = segundo

terceiro = int(input('Digite o terceiro número: '))

if terceiro > maior:
    maior = terceiro
if terceiro < menor:
    menor = terceiro

print('-=-'*10)
print('Números Digitados')
print('Primeiro: {}'.format(primeiro))
print('Segundo: {}'.format(segundo))
print('Terceiro: {}'.format(terceiro))
print('-=-'*10)
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))

