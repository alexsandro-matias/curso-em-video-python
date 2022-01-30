# interact help
# help()
# help(input)

# outra forma é usando o doc interno ou __doc__
# print(input.__doc__)


# docstring - string de documentação (manual)
# def contador(i, f , p): #parâmetros formais
#     c = i
#     while c <= f:
#         print(f'{c}' , end='..')
#         c+=p
#     print('terminado')

# contador(2,10,2)

# help(contador) -
# Saída - Help on function contador in module __main__:
# ou seja, não tem nenhuma função da função devido a não ser explicitado.
# contador(i, f, p)
    # docstring - string de documentação (manual)

# para isso, o texto deve estar entre """ no início da função.

# def contador(i, f , p): #parâmetros formais
#     """
#     Faz uma contagem e mostra na tela
#
#     :param i: Início da contagem
#     :param f: Fim da contagem
#     :param p: Passo da contagem
#     :return: Sem retorno
#     """
#     c = i
#     while c <= f:
#         print(f'{c}' , end='..')
#         c+=p
#     print('terminado')
#
# # Neste momento, se quisermos mostrar ajuda sobre o comando,
# # será exibido a sua respectiva documentação.
#
# help(contador)




# Parâmetros opcionais
# Assinatura anterior da Função.
# def somar(a,b,c):
#     soma = a + b + c
#     print(f'A soma vale {soma}')


# Assinatura posterior da Função.
# def somar(a,b,c =0):
#     soma = a + b + c
#     print(f'A soma vale {soma}')


# somar(3,2,5)

# Mas se quisermos passar menos parâmetros como no exemplo abaixo.
# Teremos um problema.
# somar(8,4)

# Com a nova assinatura da função, quando não for passado o terceiro argumento,
# o valor padrão será o declarado na assinatura da função.
# Da mesma forma que todos os parâmetros fossem opcionais.
# def somar (a = 0 , b = 0 , c = 0):


# outra forma seria nomeiar diretamente na chamada da função:
# somar(2, b = 1, a = 7)



# Escopo de declaração de variáveis
# Local onde uma variável vai existir ou deixar de existir.

# def teste(b):
#     # a = 8
#     # Para forçar que a variável "a" se torne global,
#     # usamos a palavra reservada global
#     global a
#     b += 4
#     c = 2
#     print(f'A dentro vale {a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')
#
# a = 5
# teste(a)
# print(f'A fora vale {a}')




# Retorno de valores
# A palavra reservada return
# indica que existe um retorno de algum valor (resultado) de uma função.
# Utilizando a mesma função soma, só que adicionando um retorno:

def somar(a,b,c =0):
    soma = a + b + c
    return soma

adicao = somar(3,2,5)
print(f'A soma vale {adicao}')


# Outra forma seria já colocar o retorno da função diretamente dentro do print()
print(somar(1,2,3))


# Desafio 101:
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.







# Desafio 102
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show,
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.





#
#
#
# Desafio 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
#
#
#
#
#
# Desafio 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
#
#
#
#
# Desafio 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#
# – Quantidade de notas
# – A maior nota                                                                                                                                                            
# – A menor nota                                                                                                                                                              
# – A média da turma
# – A situação (opcional)
#
#
#
#
#
# Desafio 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
