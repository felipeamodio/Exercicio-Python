# Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3 and num2 > num3:
    print("O maior é o {} e o menor é o {}".format(num1, num3))
elif num1 > num2 and num1 > num3 and num3 > num2:
    print("O maior é o {} e o menor é o {}".format(num1, num2))
elif num2 > num1 and num2 > num3 and num1 > num3:
    print("O maior é o {} e o menor é o {}".format(num2, num3))
elif num2 > num1 and num2 > num3 and num3 > num1:
    print("O maior é o {} e o menor é o {}".format(num2, num1))
elif num3 > num1 and num3 > num2 and num1 > num2:
    print("O maior é o {} e o menor é o {}".format(num3, num2))
elif num3 > num1 and num3 > num2 and num2 > num1:
    print("O maior é o {} e o menor é o {}".format(num3, num1))