# Desafio 53
# Crie um programa uma frase qualquer
# e diga se ela é um palíndromo,
# desconsiderando os espaços.
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA

texto_original = 'ana'
texto = texto_original

#tirando os espaços vazios
texto = texto_original.replace(' ', '')


for letra in texto[::]:
    texto.ap

invertido = []

for letra in texto[::-1]:
    invertido.append(letra)


print(invertido)
print(texto)

if id(texto) == id(invertido):
    print("{} é um palíndromo".format(texto_original))
else:
    print("{} não é um palíndromo".format(texto_original))
