# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino,
# M - Masculino, Sexo Inválido.

sexo = str(input("F - FEMININO\nM - MASCULINO\nInforme o sexo: "))

if sexo == "F":
    print("Você é do sexo feminino")
elif sexo == "M":
    print("Você é do sexo masculino")
else:
    print("Sexo indefinido")

