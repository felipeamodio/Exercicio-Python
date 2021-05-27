# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre
# o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS
# e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# Salário bruto : R$
# IR (11%) : R$ 0,11
# INSS (8%) : R$ 0,08
# Sindicato (5%) : R$ 0,05
# Salário líquidoL R$
#OBS: salario bruto - descontos = salario liquido

valorPorHora = float(input("Informe o valor que você ganha por hora: "))
horasTrabalhadas = float(input("Informe a quantidade de horas trabalhadas no mês: "))

salarioBruto = valorPorHora * horasTrabalhadas

print("Seu salário bruto é de R${} por mês".format(salarioBruto))

op = 0

while salarioBruto > 0:
    print("1 - Desconto do IR")
    print("2 - Desconto do INSS")
    print("3 - Desconto do Sindicato")
    print("4 - Valor do salário líquido")
    op = int(input("Escolha uma opção: "))

    if op == 1:
        ir = round(salarioBruto * 0.11)
        print("O desconto do IR é de R${}".format(ir))
    elif op == 2:
        inss = round(salarioBruto * 0.8)
        print("O desconto do iNSS é de R${}".format(inss))
    elif op == 3:
        sind = round(salarioBruto * 0.5)
        print("O desconto do sindicato é de R${}".format(sind))
    elif op == 4:
        descontos = (salarioBruto - ir) - (salarioBruto - inss) - (salarioBruto - sind)
        print("O salário líquido é de R${}".format(descontos))
    elif op == 5:
        print("Obrigado pela visita!")
print("Preciso refazer")