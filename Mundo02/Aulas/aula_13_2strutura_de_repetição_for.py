# for i in range(1, 6): # não considera o 6 -> 5 iterações
#     print('oi')
#
# for i in range(0, 6): # 6 iterações
#     print(i)
#
# for i in range(1, 7): # 6 iterações
#     print(i)

#
# for i in range(6,0,-1):
#     print(i)
#
# for i in range(0,7,2):
#     print(i)


# inicio = int(input('Ínicio: '))
# final = int(input('Final: '))
# passo = int(input('Passo: '))
# for i in range(inicio,final,passo):
#     print(i)

soma = 0
for i in range(0,4):
    n = int(input('Digite um valor: '))
    soma += n
print('A soma dos valores digitados vale: {}'.format(soma))

