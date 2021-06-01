# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
# decisão é sempre pelo mais barato.

prod1 = float(input("Digite o preço do macarrão: "))
prod2 = float(input("Digite o preço do leite: "))
prod3 = float(input("Digite o preço do pão: "))

if prod1 < prod2 and prod1 < prod3:
    print("Você deve comprar o macarrão")
elif prod2 < prod1 and prod2 < prod3:
    print("Você deve comprar o leite")
elif prod3 < prod1 and prod3 < prod2:
    print("Você deve comrpar o pão")