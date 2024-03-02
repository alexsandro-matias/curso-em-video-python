# Desafio 49 -
# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

numero = int(input('Digite um número que gostaria da tabuada: '))
for i in range(1,11):
    print('{} X {} = {}'.format(numero,i,numero*i))