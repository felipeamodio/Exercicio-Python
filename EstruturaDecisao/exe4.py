# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Digite uma letra do alfabeto: "))

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("Você digitou a letra {} e ela é uma vogal".format(letra))
else:
    print("Você digitou a letra {} e ela é uma consoante".format(letra))