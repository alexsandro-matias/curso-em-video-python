# desafio 079
# Crie um programa onde o usuário possa digitar vários números
# e cadastre-os em uma lista. Caso o número já exista lá dentro
# ele não será adicionado. No final, serão exibidos todos os valores
# únicos digitados, em ordem crescente.

# Valor adicionado com sucesso. Quer continuar? [S/N]
# Valor duplicado! Não é possível adicioná-lo. Quer continuar? [S/N]

flag = 's'
numeros = []

while flag != ('n' or 'N'):
    temporario = int(input('Digite um número: '))

    if temporario in numeros:
        print('Valor duplicado! Não é possível adicioná-lo.')

    else:
        numeros.append(temporario)
        print('Número {} adicionado com sucesso à lista.'.format(temporario))

    flag = (input('Quer continuar? [S/N]'))


print("Os valores ordendados sem repetição foram {}".format(sorted(numeros)))