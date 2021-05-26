# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7


genero = input("Informe seu gênero, H - Homem ou M - Mulher: ")


if genero == "H":
    alturaHomem = float(input("Informe sua altura em metros: "))
    calcularHomem = round((72.7 * alturaHomem) - 58, 2)
    print("Seu peso ideal é de {} quilos de acordo com sua altura".format(calcularHomem))
elif genero == "M":
    alturaMulher = float(input("Informe sua altura em metros: "))
    calcularMulher = round((62.1 * alturaMulher) - 44 ,2)
    print("Seu peso ideal é de {} quilos de acordo com sua altura".format(calcularMulher))