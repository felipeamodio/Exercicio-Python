# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou T-Tarde ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print("Em que período você estuda?")
periodo = str(input("M - Matutino\nT - Tarde\nN - Noturno\nInforme o período: "))

if periodo == 'M':
    print("Bom dia, Felipe!")
elif periodo == 'T':
    print("Boa tarde, Felipe!")
elif periodo == 'N':
    print("Boa noite, Felipe!")
else:
    print("Valor indefinido!")