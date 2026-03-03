# cria ima lista com nomes

print("Digite os nomes")

lista_nomes = []  # inicializa a lista

for i in range(3):
    nome = input("Digite um nome: ")
    lista_nomes.append(nome)

print("Sua relação de nomes:")
for nome in lista_nomes:
    print("-", nome)

    

alvo = input("Digite o nome que deseja remover: ").strip()

# procura o índice do nome ignorando maiúsculas/minúsculas
indice = next((i for i, n in enumerate(lista_nomes) if n.lower() == alvo.lower()), None)

if indice is not None:
    removido = lista_nomes.pop(indice)
    print(f'"{removido}" removido com sucesso.')
else:
    print('Nome não encontrado.')

print("Lista atualizada:", lista_nomes)

