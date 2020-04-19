# desafio 082
# Crie um programa que vai ler vários números e colocar em uma lista
# Depois disso, crie duas listas extras que vão conter apenas valores pares
# e os valores ímpares digitados respectivamente
# Ao final, mostre o conteúdo das três listas geradas


# Lista de testes
numeros = [10, 5, 11, 12, 8, 9]
pares = []
impares = []
flag = 'S'


# numeros = []
# while flag != ('n' or 'N'):
#     numeros.append(int(input('Digite um número: ')))
#     flag = input("Deseja continuar: [S/N]")

for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print("Lista completa: {}".format(numeros))
print("Lista de números pares: {}".format(pares))
print("Lista de números ímpares: {}".format(impares))