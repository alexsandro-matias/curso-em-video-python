# Desafio 026
# Faça um programa que leia uma frase pelo teclado e mostre:
#
# Quantas vezes aparece a letra "a";
#
# Em que posição ela aparece a primeira vez
#
# Em que posição ela aparece a última vez

frase = (input('Digite uma frase qualquer: ')).lower().strip()
print('A letra "a" aparece no texto digitado {} vezes'.format(frase.count('a')))
print('A primeira posição que a letra "A": {}'.format(frase.find('a')))
print('A última posição que a letra "A": {}'.format(frase.rfind('a')))
