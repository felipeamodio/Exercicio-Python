# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

fahrenheit = float(input("Informe a temperatura em Fahrenheit: "))

celsius = round((fahrenheit - 32) / 1.8, 2)

print("A temperatura de {}° Fahrenheit convertida fica em {}° Celsius".format(fahrenheit,celsius))