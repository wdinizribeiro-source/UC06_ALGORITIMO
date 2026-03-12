import requests
#  api
url = "https://rickandmortyapi.com/api/character"

resposta = requests.get(url)

print (resposta)
# json é o formato do codigo pra obter a resposta
json = resposta.json()

print(json)
personagem =json["results"] 

print(personagem)

#  laço de repetição para consultar apenas nomes dos personagem

for nome_personagem in personagem:
    print(nome_personagem["name"])


#  retornar mais informações além do nome
for mais_info in personagem:
    print("nome: ", mais_info["name"])
    print("status: ", mais_info["status"])
    print("especie: " , mais_info["species"])
    print("---------------------------")

# pedir ao usuario para digitar um id e retornar da ApI o personagem referente esse ID
id = int(input("Digite um numero inteiro: "))
link_api = f"https://rickandmortyapi.com/api/character/{id}"

resposta = requests.get(link_api)

novo_json = resposta.json()
print("nome: ", novo_json["name"])
print("status: ", novo_json["status"])
print("especie: " , novo_json["species"])
print("---------------------------")

# data de entre
# criar um menu para seleção
# 1 consultat por id
# 2 consultar por nome
# 3 lista de personagem

#  se for opção 1 
"""
pedir ao usuario para digitar um id (numero inteiro)e retornar de 
dentro da api o persdonagem referente ao id digitado
retorne todas as informações sobre o personagem
"""

# se for a opção 2
"""
pedir ao usuario para digitar um nome e retornar de 
dentro da api o persdonagem referente ao nome digitado

obs de codigo: para percorrer o json  e retornar o nome digitado
"""
#  for personagem in dados ["results"]
# retornar todos os personagens