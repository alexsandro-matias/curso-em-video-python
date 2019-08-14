# Desafio 022
# Crie um programa que leia o nome completo de uma pessoa e mostre:

# Nome com todas as letras maiúsculas
#
# Nome com todas letras minúsculas
#
# Quantas letras do nome completo(sem considerar os espaços)
#
# Quantas letras tem o primeiro nome


# nomeCompleto = input('Digite seu nome completo: ')

# Já começar a leitura com String fateada
nomeCompleto = str(input('Digite seu nome completo: ')).strip()
print('Nome em letras Maiúsculas: {}'.format(nomeCompleto.upper()))
print('Nome em letras Minúsculas: {}'.format(nomeCompleto.lower()))


print('Quantidade de letras do nome: {}'.format(len(nomeCompleto)-nomeCompleto.count(' ')))
print('Quantidade de letras do primeiro nome: {}'.format(len(nomeCompleto[0])))


