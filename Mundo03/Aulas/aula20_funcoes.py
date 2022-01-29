# Funções em python também pode ser chamadas de rotinas
# que são ações que são repetidas constantemente.

# def ou definição de função, é a palavra reservada para definir as funções.
#
# def mostrar_linha():
#     print('_' * 30)
#
# def boas_vindas(mensagem):
#     mostrar_linha()
#     print('\t' + mensagem)
#     mostrar_linha()
#
#
# nome = 'Alexsandro'
#
# boas_vindas(nome)


# em pythom existe um conceito de empacotamente de parâmetros.
# Ou seja, em funções onde não é definida a quantidade de parâmetros.
# Por exemplo se for criada uma função que conte a quantidade de parâmetros que foram passados.

# def contador(*numeros):
#     print(f'Quantidade de parâmetros passados: {len(numeros)}')
#
# contador(1, 2, 4)
# contador(1, 2, 3 , 5 , 9)

# def dobra (lista):
#     for i in range(len(lista)):
#         lista[i] *= 2
#     print(lista)
#
#
# valores = [7,2,5,0,4]
# dobra(valores)


# def soma(*numeros):
#     somatorio = 0
#     for i in numeros:
#         somatorio += i
#     print(somatorio)
