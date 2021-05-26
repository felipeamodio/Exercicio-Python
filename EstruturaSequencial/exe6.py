# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

valorPorHora = float(input("Informe o valor que você ganha por hora: "))
horasTrabalhadas = float(input("Informe a quantidade de horas trabalhadas no mês: "))

salario = valorPorHora * horasTrabalhadas

print("O valor do seu salário é de R${} de acordo com a quantidade de {} horas trabalhadas nesse mês e o valor por hora de R${}".format(salario,horasTrabalhadas,valorPorHora))
