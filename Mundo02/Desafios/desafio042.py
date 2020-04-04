# Desafio 042
# Refaça o desafio 35 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado.


primeiro = float(input('Digite o primeiro lado do triângulo: '))
segundo = float(input('Digite o segundo lado do triângulo: '))
terceiro = float(input('Digite o terceiro lado: '))

if (primeiro == segundo) and (segundo == terceiro):
    print('O triângulo é equilátero.')

if primeiro != segundo and segundo != terceiro and primeiro != terceiro:
    print('O triângulo é escaleno.')

if (primeiro == segundo and segundo != terceiro) or (primeiro != segundo and primeiro == terceiro) or (primeiro != segundo and segundo == terceiro):
    print('O triângulo é isóceles.')
