#  crie um afunção que receba 5 notas de um aluno e calcule e retorne a media
#  crie uma função para receber a media do aluno e retorne se ele esta aprovado ou reprovado


print("Digite as 5 notas:")

nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))
nota3 = int(input("Digite a nota 3: "))
nota4 = int(input("Digite a nota 4: "))
nota5 = int(input("Digite a nota 5: "))


def media (nota1, nota2, nota3, nota4, nota5):
    return  nota1 + nota2 + nota3 + nota4 + nota5 /5
resultado = media(nota1, nota2, nota3, nota4, nota5)
print(f"A média é: {resultado:.2f}")

if resultado >=10:
    print("Aprovado")
else:
    print("reprovado")