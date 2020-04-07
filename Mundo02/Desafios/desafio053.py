# Desafio 53
# Crie um programa uma frase qualquer
# e diga se ela é um palíndromo,
# desconsiderando os espaços.
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA

texto_original = 'O LOBO AMA O BOL'
texto = texto_original

#tirando os espaços vazios
texto = texto_original.replace(' ', '')

invertido = []

# Adicionando cada letra à String invertida
for letra in texto[::-1]:
    invertido.append(letra)

#juntando a lista e convertendo-a em String
invertido = ''.join(invertido)

# Se o lido ao contrário for igual ao igual o texto digitado,
# Ele será um palíndromo
if texto == invertido:
    print("{} é um palíndromo".format(texto_original))
else:
    print("{} não é um palíndromo".format(texto_original))
