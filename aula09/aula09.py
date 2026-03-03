
nome = "Beltrano"
# criando uma função
# parametros sempre vão dentro de parenteses()
def saudacao(nome):
    print("Olá,",nome, "Seja bem vindo")
#  chamar uma função
saudacao(nome)

# recebe dois valores , faz a soma e retorna resultado
def soma(valor1, valor2):
    return valor1+valor2

print(soma(1457,10))

salario_funcionario = 1600
beneficio = 200
novo_salario = soma(salario_funcionario, beneficio)
print(novo_salario)

# soma dois valores de a idade do usuario for igual ou a maior a 18
# se não mostrar mensagem -" sua idade é menor que 18"
idade_usuario = int(input("digite sua idade :"))
if idade_usuario >= 18:
    var1 = int(input("digite o primeiro valor :"))
    var2 = int(input("digite o segundo valor :"))
    resultado = soma(var1, var2)
    print(resultado)
else:
    print("sua idade é menor que 18")
# retorna a quantidade de informaçãoe contida na lista
lista = [20, 1, 6, 10, 45]
print(len(lista))

#  sum - soma toda lista numerica

print(sum(lista))

# MAX - retorna o maior valor
print(max(lista))

# MIN -  retorna o menor valor
print(min(lista))

# ORDENAR
print(sorted(lista))

# TYPE - retorna o tipo
tipo = 10
print(type(tipo))

# conversoes do tipo converte para flutuante ou para inteiro ou texto
print(float(tipo))

#  crie um afunção que receba 5 notas de um aluno e calcule e retorne a media
#  crie uma função para receber a media do aluno e retorne se ele esta aprovado ou reprovado