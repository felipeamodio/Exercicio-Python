# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input("Informe a nota de Matemática: "))
nota2 = float(input("Informe a nota de Português: "))
nota3 = float(input("Informe a nota de Informática: "))
nota4 = float(input("Informe a nota de Química: "))

media = round((nota1 + nota2 + nota3 + nota4) / 4, 2)

print("A media das notas são: {}".format(media))