nome = input("Digite o seu nome:")
idade = int (input( "digite a idade:"))
cidade = input("digite a cidade:")

cadastro = {
    "nome": nome,
    "idade": idade,
    "cidade": cidade
}


print("Nome:", cadastro["nome"])
print("Idade:", cadastro["idade"])
print("Cidade:", cadastro["cidade"])

print ("informe as Notas")

nota01 = float(input("Informe a nota 1: "))
nota02 = float(input("Informe a nota 2: "))
nota03 = float(input("Informe a nota 3: "))
nota04 = float(input("Informe a nota 4: "))
nota05 = float(input("Informe a nota 5: "))


media = (nota01 + nota02 + nota03 + nota04 + nota05) / 5

print("Média:", media)
