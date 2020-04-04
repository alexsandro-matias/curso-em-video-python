# módulos são adicionados para algumas funcionalidades específicas,
# já que o Python por padrão não vem completo (built-in), ou seja, um número limitado de comandos. O objetivo de é performance.
# Nesse caso, precisamos de módulos (pacotes). Para inclusão de alguma biblioteca,
# é necessário a palavra reservada import.
# O uso pode ser de forma completa (toda a biblioteca), através da forma:
# import math


# ou de forma específica, ou importação otimizada
from math import ceil
# Neste caso, a importação serve para fazer o arrendondamento para cima.
# Mesmo ela contento essa biblioteca, não preciso importar toda a biblioteca,
# poupando um pouco mais de memória. Já para fazer o arrendondamento para baixo, utiliza-se a floor.
# Mais funcionalidades:
# trunc - truncar - eliminar a casa decimal.
# pow - potência - potência.
# sqrt - square root - raiz quadrada.
# factorial - fatorial.

# # De forma completa para cálculo da raiz quadrada:
# import math
# numero = float(input('Digite um número: '))
# raiz = math.sqrt(numero)
# #
# # Arreondando para cima
# print('A raiz de {} é {}'.format(numero, math.floor(raiz)))
#
# # De forma otimizada
# from math import sqrt, ceil, trunc, floor
# print('A raiz de {} é {}'.format(numero, raiz))
# numero = float(input('Digite um número: '))
# raiz = math.sqrt(numero)
# print('A raiz de {} é {}'.format(numero, raiz))

# Exemplo para números aleatórios usando a biblioteca random
import random
num = random.randint(1,10)
print(num)



# Para ter acesso às bibliotecas possíveis de serem importas, iremos no site:
# https://pypi.org/


# Desafios 16 ao 21
