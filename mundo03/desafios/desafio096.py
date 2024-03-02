# desafio 096
# faça um programa que tenha uma função chamada area(),
# que receba as dimensões de um terreno retangular (largura e comprimento)
# e mostre a área do terreno.


# controle de Terrenos
# _____________________

# largura (m): 4.5
# comprimento (m): 8
# A área de um terreno 4.5 X 8.0 é de 36.0 m².

def area_terreno(largura, comprimento):
    print(
        f'A área de um terreno {largura} m X {comprimento} m é de {largura * comprimento} m²')


largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento(m): '))
area_terreno(largura, comprimento)
