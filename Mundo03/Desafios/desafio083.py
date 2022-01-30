# desafio 083
# Crie um programa onde o usuário digite uma expressão qualquer que use
# os parênteses. Seu aplicativo deverá analisar se a expressão passada está
# com os parênteses abertos e fechados na ordem correta.

expressao = list((input('Digite uma expressão algébrica: ')))
abertura = expressao.count('(')
fechamento = expressao.count(')')
print(expressao)

if abertura == fechamento:
    print('A expressão algébrica é válida.')

else:
    print('A expressão algébrica não é válida.')
