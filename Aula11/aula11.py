# criar numero aleatorio
import random
import math
import datetime

numero_aleatorio = random.randint(1000, 2000)
print(numero_aleatorio)

# sorteio de aluno

alunos =["israel", "Ademilson", "Anna", "wellington", "Jonathan", "Isabelly", "João Pedro", "Luis Felipe", "iara"," Vanessa", "Daniel","João Paulo","Lucas","Bernardo", "Camila", "stefany", "Guilherme", "Micael", "Kauan"]

sorteado = random.choice(alunos)
sorteado2 = random.choice(alunos)

# choice escolher de forma aleatoria
print("dupla dinamica", sorteado, " -", sorteado2)

# função de raiz quadrada sqrt
numero = 16387
raiz = math.sqrt(numero)
print(raiz)

# elevar um numero pow
print(math.pow(2, 2))

# trabalhar com datas e horarios

agora = datetime.datetime.now()
print(agora.year) 
# year retorna ano

# exercicio 
# solicitar ao usuario um numero de 1 a 5
# gerar um numero aleatorio utiizando biblioteca random.randit
# verificar se o usuario digitou o mesmo valor da função randit

numero_usuario = int(input("digite um numero da sorte de 1 a 5:"))
numero_sorte = random.randint(1, 200)
if numero_usuario == numero_sorte:
    print("parabens você ganhou um aperto de mão e 2 reais")
else:
    print("errou, tente novamente")

