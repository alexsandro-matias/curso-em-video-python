# Desafio 044
# Elabore um programa que calcule o valor a ser
# pago por um produto considerando o seu preço normal e condições de pagamento:
# - Á vista no dinheiro ou cheque: 10% de desconto;
# - Á vista no cartão: 5% de desconto;
# - Até 2X no cartão: Preço normal;
# - 3X ou mais no cartão: 20% de juros.


preco_normal_produto = float(input("Digite o valor inicial do produto em R$: "))
print("-------------------------------------------------------------------")
print("-------------------Escolha a forma de pagamento--------------------")
print("1. Á vista no dinheiro ou cheque: 10% de desconto")
print("2. Á vista no cartão: 5% de desconto")
print("3. Até 2X no cartão: Preço normal")
print("4. 3X ou mais no cartão: 20% de juros")

print("-------------------------------------------------------------------")
forma_pagamento = int(input("Informa a forma de pagamento: "))

if forma_pagamento == 1:
    preco_final = preco_normal_produto * 0.9
    print(f"Preço final do produto: R${preco_final:.2f}")
elif forma_pagamento == 2:
    preco_final = preco_normal_produto * 0.95
    print(f"Preço final do produto: RR${preco_final:.2f}")
elif forma_pagamento == 3:
    preco_final = preco_normal_produto
    print(f"Preço final do produto: 2X de R${preco_final / 2:.2f}")
else:
    preco_final = preco_normal_produto * 1.2
    print(print(f"Preço final do produto: 3X de R${preco_final / 3:.2f}"))
