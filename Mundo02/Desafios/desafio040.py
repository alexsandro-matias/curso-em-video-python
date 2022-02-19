# Desafio 040
# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com média atingida:
# - Média abaixo de 5,0 = REPROVADO
# - Média entre 5,0 e 6,9 = RECUPERAÇÃO
# - Média 7,0 ou superior = APROVADO

from string import octdigits


nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Aluno aprovado.")

elif media >= 5 and media < 6.9:
    print("Aluno em recuperação.")

else:
    print("Aluno reprovado.")


