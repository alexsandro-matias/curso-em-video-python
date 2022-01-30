

frase = "Curso em Vídeo Python"

# print(type(frase))
# <class 'str'>



# # # Fateamento
# # posição 9
# print(frase[9])

# # Intervalo sem o último elemento, sem o 13
# print(frase[9:13])

# # Intervalo sem o último elemento, para o 13
# print(frase[9:14])

# # Mesmo se intervalor for ultrapassado
# print(frase[9:21])

# # Mesmo se intervalor for ultrapassado
# print(frase[9:21])

# # Mesmo se intervalor for ultrapassado, pulando de 2 em 2 (passo)
# print(frase[9:21:2])
#
# # Se omitir o primeiro caracter, ele irá considerar o frase[0]
# print(frase[:5])
#
# # Se omitir o último caracter, ele irá considerar o frase[15] até o final
# print(frase[15:])

# Neste caso, começa no frase[9] e como não foi mencionado o final,
# irá o até o fim, com o passo 3
# print(frase[9::3])

# # # Análise
# comprimento da String
# print(len(frase));

# # Contagem de uma String
# print(frase.count('Cur'))


# Contagem de uma String

# # Contagem de uma String com passos com fateamento
# print(frase.count('Cur', 0, 13))
# # contagem da String "Cur" frase[0-13]
# print(frase.count('Cur'))


# # Em que posição uma String foi encontrada
# print(frase.find('deo'))

# # Caso uma String não for encontrada, o valor retornado é -1
# print(frase.find('Android'))

# # Para verificar se uma String existe dentro da outra:
# print('Curso' in frase)

# # # Transformação
# Uma String em Python é uma lista de caracteres imutável
# Porém é possível fazer algumas transformações através dos métodos.
#
# # Para a troca de caracteres
# print(frase.replace('Python','Android'))
#
# # Para a troca para caixa alta
# print(frase.upper())

# # Para a troca para caixa baixa
# print(frase.lower())

# # Para a troca para caixa capitalizada
# # Tudo minúsculo e somente a primeira letra fica maiúscula.
# print(frase.capitalize())
#
# # Para a troca para primeira letra depois do espaço fica maiúscula.
# print(frase.title())
#
# # Para a remoção dos espaços vazios antes e depois do texto
# print(frase.strip())

# # Para a remoção dos espaços vazios depois do texto
# # (right - direita)
# print(frase.rstrip())
#
# # Para a remoção dos espaços vazios antes do texto
# # (left - esquerda)
# print(frase.lstrip())
#

# # # Divisão de uma String
#  Para separar uma String
print(frase.split()[0])
print(frase.split()[0][1])

# Esse método cria uma lista com o conjunto de palavras descritas na String

# Para junção de Strings
frase = '*'.join(frase)
print(frase)
