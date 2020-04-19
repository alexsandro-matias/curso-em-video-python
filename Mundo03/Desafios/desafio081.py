# desafio 081
# crie um programa que vai ler vários números e colocar numa lista
# Depois, mostre:
# a) Quantos números foram digitados
# b) A lista de valores, ordenadas de forma descrecente
# c) Se o valor 5 foi digitado e está ou não na lista.

# numeros = []

# Lista de Teste


flag = 's'


numeros = [11, 10, 9, 5, 0]
# while flag != ('n' or 'N'):
#     numeros.append(int(input('Digite um valor: ')))
#     flag = input('Deseja continuar: [S/N]')

print("Quantidade de números digitados: {} ".format(len(numeros)))
print("Lista em ordem decrescente: {}".format(sorted(numeros,reverse=True)))

if 5 in numeros:
    print("O número 5 está na lista.")
else:
    print("O número 5 não pertence à lista.")
