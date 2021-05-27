#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de
# São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que
# leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além
# do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as
# mensagens adequadas.

mediaPeixe = 50
multa = 4
op = -1

while op != 3:
    print("#### INFORME A OPÇÃO DESEJADA ####")
    print("1 - Cadastrar peso de peixe")
    print("2 - Calcular o preço da multa")
    print("3 - Sair")
    op = int(input("Informe sua opção: "))

    if op == 1:
        pesoPeixe = float(input("Informe o peso do peixe em quilos: "))
    elif op == 2:
        pesoMedia = pesoPeixe * multa
        if pesoPeixe > 50:
            print("O peixe está com o peso acima da média e será necessário pagar R${}".format(pesoMedia))
        else:
            print("O peixe está com o peso dentro da média, não será necessário pagar multa!!")
    elif op == 3:
        print("Encerrar")

print("Obrigado pelo cadastro de peso de peixe. Volte sempre!")

