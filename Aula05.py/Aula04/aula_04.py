# nome = input("Digite o seu nome:")
# print("seu nome é ", nome)
# int = inteiros
#  float = decimais

# numero = int (input( "digite de 1 a 10"))
# soma = numero + 10 
# print(soma)

# calculo_salario =float(input("digite seu salario"))
# soma_salario = calculo_salario * 3.5
# print(soma_salario)

# idade =  20 

# if idade >= 18:
#     print("sua idade é", idade)

# 

# valida_idade = int(input("digite sua idade:"))
# if valida_idade <18:
#     print("Você é menor de idade precisa presença dos pais")
# else:
#     print("você á maior de idade, pode entrar")

#  IF  - ELIF - ELSE

# nota = int(input("digite a nota do aluno:"))
# nome_aluno =input("digite o nome do aluno:")
# if nota >= 9:
#     print(f"o aluno {nome_aluno}esta aprovado com a nota: {nota}")
# elif nota >=7 and nota <=8:
#     print(f"o aluno {nome_aluno}esta aprovado por conselho com a nota{nota}")
# else : 
#     print(f"o aluno {nome_aluno} esta Reprovado com a nota:{nota}")

#  se o usuario for menor de idade entao ele precisa ter autorização
#  se o usuario for maior de idade ele precisa ter a altura minima

# idade_cliente = int(input("digite a idade do cliente: "))
# altura_cliente = float(input("digite a altura do cliente: "))
# if idade_cliente <18:
#     print(" o cliente é menor de idade e não pode entrar no brinquedo")
# else:
#     if altura_cliente >=1.50:
#         print("Você é maior de idade e tem a altura minima para o brinquedo")
#     else:
#         print("você mesmo sendo maior de idade, tem menos de 1.50 de altura e não pode ir no brinquedo")
#     # print("cliente maior de idade, pode subir no brinquedo")

valida_idade = 17
# condicional ternario
status = print("menor de idade") if valida_idade < 18 else print ("maior de idade")
print (status)
    