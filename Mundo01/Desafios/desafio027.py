# Desafio 027
# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente:
#
# Ex: Ana Maria de Souza
# Primeiro = Ana
# Segundo = Souza


# Forma mais otimizada

nomeCompleto = str(input('Digite o nome completo da pessoa: ')).split()
print("Primeiro Nome: {}".format(nomeCompleto[0]))
print("Último Nome: {}".format(nomeCompleto[len(nomeCompleto) - 1]))

#
#
# nomeCompleto = 'Francisco Márcio Moura Borges de Azevedo'
# primeiroNome = nomeCompleto.split()
#
# #Primeiro Nome estará na posição [0] da lista
# primeiroNome = primeiroNome[0]
# print('Primeiro Nome: {}'.format(primeiroNome))
#
# # Preciso saber a quantidade de posições que tem o nome.
# quantidadePosicoes = (len(nomeCompleto.split()))
#
# posicaoUltimoNome = quantidadePosicoes - 1
# #quantidade de posições ou, podemos dizer, quantidade de palavras.
# #Já o último nome estará última posição da lista. Logo, [comprimento - 1]
# ultimoNome = nomeCompleto.split()
# ultimoNome = ultimoNome[posicaoUltimoNome]
# print('Último Nome: {}'.format(ultimoNome))
