# Escreva um programa que converta uma temperatura digitada de ºC para ºF.
celsius = float(input('Informe a temperatura em ºC: '))
farenheint = (9*celsius/5) + 32
print("A temperatura {:.1f}ºC equivale a {:.1f}ºF.".format(celsius, farenheint))
