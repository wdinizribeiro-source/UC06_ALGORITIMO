
print("Programa Cadastro:")

# Coleta de dados
nome = input("Digite o nome: ").strip()
idade = input("Digite a idade: ").strip()

# Validação simples (opcional)
if not nome:
    print("Nome não pode ser vazio.")
elif not idade.isdigit():
    print("Idade precisa ser um número inteiro.")
else:
    # Abre o arquivo e escreve uma linha "Nome - Idade"
    # Use 'a' para acrescentar sem apagar o conteúdo anterior.
    with open("aula10/cadastro.txt", "a", encoding="utf-8") as arq:
        arq.write(f"{nome} - {idade}\n")
    print("Cadastro salvo com sucesso!")
