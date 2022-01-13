numeros = [[], []]

intermediario = 0

for numero in range(1, 6):
    intermediario = int(input(f"Digite o {numero}o. valor: "))
    if intermediario % 2 == 0:
        numeros[0].append(intermediario)
    else:
        numeros[1].append(intermediario)

