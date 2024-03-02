numeros = [[], []]

intermediario = 0

for numero in range(1, 6):
    intermediario = int(input(f"Digite o {numero}o. valor: "))
    if intermediario % 2 == 0:
        numeros[0].append(intermediario)
    else:
        numeros[1].append(intermediario)

print(f'Lista dos números pares: {numeros[0]}')
print(f'Lista dos números ímpares: {numeros[1]}')



# desafio 84
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo dentro de uma lista.
# No final mostre:
# a) Quantas pessoas foram cadastradas;
# b) Uma listagem com as pessoas mais pesadas.
# c) Uma listagem com as pessoas mais leves.
resposta = "s"

nome = input("Nome: ")
peso = float(input("Peso: "))
resposta = input("Quer continuar? [S | N]: ")

print("-=" * 60)
print("Ao todo, você cadastrou {} pessoas")
print("O maior peso foi de {} kg. Peso de {}.")
print("O menor peso foi de {} kg. Peso de {}.")

# desafio 86
# Crie um programa uma matriz de dimesão 3 X 3 com os valores preenchidos pelo teclado.
print("Digite um valor para [0,1]")  # [ 1 ] [ 1 ] [ 1 ]

# # desafio 87
# realize o desafio anterior, mostrando no final:
# a) A soma de todos os valores pares digitados;
# b) A soma dos valores da terceira coluna;
# c) O maior valor da segunda linha.


# # desafio 88
# Faça um programa que ajude um jogar da megasena a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai perguntar
# quantos jogos serão sorteados 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo numa lista composta.

# timer -
