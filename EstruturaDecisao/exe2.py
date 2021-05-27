# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = int(input("Informe um valor negativo ou positivo: "))

if valor < 0:
    print("O valor é negativo")
elif valor > 0:
    print("O valor é positivo")
elif valor == 0:
    print("O valor é neutro")