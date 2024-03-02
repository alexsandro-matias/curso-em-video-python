#
# Desafio 035
# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.
#

ExisteTriangulo = False

primeiro = float(input('Digite o valor do primeiro segmento de reta: '))
maior = primeiro

segundo = float(input('Digite o segundo: '))
if segundo > maior:
    maior = segundo

terceiro = float(input('Digite o terceiro: '))
if terceiro > maior:
    maior = terceiro


if primeiro == maior:
    if primeiro < (segundo + terceiro):
        ExisteTriangulo = True

if segundo == maior:
    if segundo < (primeiro + terceiro):
        ExisteTriangulo = True


if terceiro == maior:
    if terceiro < (primeiro + segundo):
        ExisteTriangulo = True

if ExisteTriangulo:
    print("É possível formar um triângulo")
else:
    print("Não é possível formar um triângulo")
