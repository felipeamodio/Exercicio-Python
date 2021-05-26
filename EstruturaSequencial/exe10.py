# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Informe sua altura em metros: "))

pesoIdeal = round((72.7 * altura) - 58, 2)

print("O seu peso ideal é {} quilos de acordo com a sua altura".format(pesoIdeal))