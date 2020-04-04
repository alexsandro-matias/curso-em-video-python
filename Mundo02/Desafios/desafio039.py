# Desafio 039
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a idade:
# - Se ele ainda vai se alistar ao serviço militar;
# - Se é hora de se alistar;
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


from datetime import date
ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento


print('Quem nasceu em {} tem {} anos em {} '.format(ano_nascimento, idade, ano_atual))

if idade < 18:
    diferenca = 18-idade
    print('Ainda falta(m) {} anos para o alistamento'.format(diferenca))
    print('Seu alistamento será em {}'.format(diferenca+ano_atual))

else:
    diferenca = ano_atual - 18
    print('Você já deveria ter se alistado há {} anos'.format(diferenca - ano_nascimento))
    print('Seu alistamento foi no ano de {}'.format(diferenca))
