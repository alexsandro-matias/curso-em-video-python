# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'm' ou ''f.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


sexo = input('Informa o sexo da pessoa: ')

while sexo not in 'FfMm':
    print('Valor digitado inválido. Digite a letra "M" ou "F".')
    sexo = input('Informa o sexo da pessoa: ')
    print(sexo)

if sexo in 'mM':
    print('A pessoa é do sexo masculino')
else:
    print('A pessoa é do sexo feminino.')
