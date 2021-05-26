# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input("Informe a temperatura em Celsius: "))

fahrenheit = round((celsius * 1.8) + 32, 2)

print("A temperatura de {}° Celsius convertida fica em {}° Fahrenheit".format(celsius,fahrenheit))