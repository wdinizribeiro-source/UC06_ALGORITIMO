
import sys
import time
import requests

BASE_URL = "https://rickandmortyapi.com/api/character"

id = int(input("Digite um numero inteiro: "))
link_api = f"https://rickandmortyapi.com/api/character/{id}"

resposta = requests.get(link_api)

novo_json = resposta.json()
print("nome: ", novo_json["name"])
print("status: ", novo_json["status"])
print("especie: " , novo_json["species"])
print("---------------------------")



nome = input("Digite o nome do personagem: ")
link_api = f"https://rickandmortyapi.com/api/character/?name={nome}"
resultado = requests.get(link_api)
nome_json = resultado.json()
for teste in nome_json["results"]:
    print("nome: ", teste["name"])
    # print("status: ", teste["status"])
    # print("especie: " , teste["species"])
    # print("---------------------------")

print("MENU")
print("1 - Consultar por ID")
print("2 - Consultar por nome")
print("3 - Lista de personagens")


opcao = int(input("Digite uma opção de 1 a 3: "))

if opcao == 1:
    print("Chamando função: consultar por ID...")
elif opcao == 2:
    print("Chamando função: consultar por nome...")
elif opcao == 3:
    print("Chamando função: lista de personagens...")
else:
    print("Opção inválida!")

import requests

BASE_URL = "https://rickandmortyapi.com/api/character"

def consultar_por_id():
    try:
        id_char = input("\nDigite o ID do personagem: ")
        resposta = requests.get(f"{BASE_URL}/{id_char}")
        
        if resposta.status_code == 200:
            dados = resposta.json()
            print(f"\n--- Personagem ID {id_char} ---")
            print(f"Nome: {dados['name']}")
            print(f"Status: {dados['status']}")
            print(f"Espécie: {dados['species']}")
        else:
            print("Erro: Personagem não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def consultar_por_nome():
    nome = input("\nDigite o nome do personagem: ")
    resposta = requests.get(f"{BASE_URL}/?name={nome}")
    
    if resposta.status_code == 200:
        dados = resposta.json()
        print(f"\n--- Resultados para '{nome}' ---")
        for personagem in dados["results"]:
            print(f"ID: {personagem['id']} | Nome: {personagem['name']} ({personagem['status']})")
    else:
        print("Erro: Nenhum personagem com esse nome foi encontrado.")

def listar_personagens():
    # Exemplo simples: lista os primeiros 20 (primeira página)
    resposta = requests.get(BASE_URL)
    if resposta.status_code == 200:
        dados = resposta.json()
        print("\n--- Lista de Personagens (Pág. 1) ---")
        for p in dados["results"]:
            print(f"ID: {p['id']} - {p['name']}")
    else:
        print("Erro ao carregar lista.")

# --- LOOP PRINCIPAL DO MENU ---
while True:
    print("\n========= MENU =========")
    print("1 - Consultar por ID")
    print("2 - Consultar por nome")
    print("3 - Lista de personagens")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        consultar_por_id()
    elif opcao == "2":
        consultar_por_nome()
    elif opcao == "3":
        listar_personagens()
    elif opcao == "0":
        print("Saindo do programa... Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")
