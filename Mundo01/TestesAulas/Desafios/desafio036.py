# Desafio 036
# Escreva um programa para aprovar o empréstimo bancário
# para compra de uma casa. O programa vai perguntar o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal,
# sabendo que ele não pode
# exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o salário da pessoa: '))
tempo = float(input('Digite o tempo em anos do financiamento: '))

prestacao = casa / (tempo * 12)
margem = salario * 0.3

print('-=-'*20)
print('INFORMAÇÕES')
print('-=-'*20)
print('Valor do Imóvel:R$ {:.2f}'.format(casa))
print('Salário do comprador:R$ {:.2f}'.format(salario))
print('Tempo de financiamento: {:.0f} anos'.format(tempo))
print('Valor da parcela:R$ {:.2f}'.format(prestacao))
print('Valor da margem:R$ {:.2f}'.format(margem))

print('-=-'*20)

if prestacao <= margem:
    print('Parabéns! Seu financiamento foi aprovado!')
else:
    print('Infelizmente seu financiamento foi negado.')
