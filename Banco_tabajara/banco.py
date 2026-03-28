
import pandas as pd
import os

caminho_excel = r"C:\Users\wellington.drribeiro\OneDrive - SENAC - SP\BANCO TABAJARA.xlsx"

# Carregar ou criar o DataFrame
if os.path.exists("banco_tabajara.xlsx"):
    df = pd.read_excel("banco_tabajara.xlsx", dtype={'CPF': str})
else:
    df = pd.DataFrame(columns=["numero_conta", "nome","CPF", "Tipo_conta", "agencia", "extrato"])


def gerar_numero_conta(df):
    if df.empty or "numero_conta" not in df.columns:
        return 1

    ultimo_numero = df["numero_conta"].max()

    if ultimo_numero >= 100:
        print("⚠️ Limite de contas atingido (máximo 100).")
        return None

    return ultimo_numero + 1


# Menu
print("================================================")
print("        BEM - VINDO AO BANCO TABAJARA")
print("================================================\n")
print("1 > Criar conta")
print("2 > Acessar conta")

opcao = int(input("R: "))

if opcao == 1:
    nome = input("Digite seu nome: ")
    cpf = str(input("Digite seu CPF: "))
    tipo_conta = input("Digite tipo de conta: ")

    # GERA NÚMERO AUTOMÁTICO
    novo_numero = gerar_numero_conta(df)

    # - numero_conta = Ser	á gerada de forma sequencial começando do 0 até 100

    if df.empty:
        numero_conta = 0
    else:
        df["numero_conta"] = df["numero_conta"].astype(int)
        numero_conta = df["numero_conta"].max() + 1

    # - agencia = será gerado de forma sequencial começando do 400 até 700

    if df.empty:
        agencia = 400
    else:
        df["agencia"] = df["agencia"].astype(int)
        agencia = df["agencia"].max() + 1

    # - extrato_bancario = valor inicial terá que começar em 0

    extrato_bancario = 0

    # Criação do dicionário com os dados
    novo_cliente = {
        "numero_conta": numero_conta,
        "nome": nome,
        "CPF": cpf,
        "Tipo_conta": tipo_conta,
        "agencia": agencia,
        "extrato": extrato_bancario
    }

    # Adiciona ao DataFrame (usando [novo_cliente] para converter em lista de um item)
    df = pd.concat([df, pd.DataFrame([novo_cliente])], ignore_index=True)

    # Salva no Excel
    df.to_excel("banco_tabajara.xlsx", index=False)
    print(f"\n✅ Conta criada com sucesso! Seu número é: {numero_conta}")

elif opcao == 2:
    # Pede o CPF ao usuário, converte para texto (str) e o .strip() remove espaços acidentais no início ou fim.
    cpf_busca = str(input("Digite seu CPF: ")).strip()
    # Pede o número da conta e converte para inteiro (int) para poder comparar com os números salvos no Excel.
    numero_busca = int(input("Digite o número da sua conta: "))

    conta = df[
        # procura linhas onde o CPF bate com o digitado
        (df["CPF"].astype(str).str.strip() == cpf_busca) &
        # procura linhas onde o número da conta bate
        (df["numero_conta"].astype(int) == numero_busca)
    ]
# O & significa que os dois precisam ser verdadeiros ao mesmo tempo

    if conta.empty:  # Se a busca não encontrou nenhuma linha, .empty retorna True e exibe mensagem de erro.
        print("\n❌ Usuário não encontrado, tentar novamente ou realizar o cadastro")
    else:
        # Se encontrou, o .iloc[0] pega a primeira linha do resultado e extrai cada coluna em uma variável separada:
        index_conta = int (conta.index[0])
        nome_cliente = conta.iloc[0]["nome"]
        agencia_cliente = conta.iloc[0]["agencia"]
        tipo_cliente = conta.iloc[0]["Tipo_conta"]
        extrato_cliente = conta.iloc[0]["extrato"]

        print("\n================================================")
        print(f"  Bem-vindo(a) BANCO TABAJARA, {nome_cliente}!")
        print("================================================")
        print(f"  Conta Nº : {numero_busca}")
        print(f"  Agência  : {agencia_cliente}")
        print(f"  Tipo     : {tipo_cliente}")
        print(f"  Saldo    : R$ {extrato_cliente:.2f}")
        print("================================================")


        extrato_cliente = conta.iloc[0]["extrato"] # inicializa antes do loop

    while True:
        print("\n===== MENU DA CONTA =====")
        print("1 - Sacar")
        print("2 - Depositar")
        print("3 - Saldo")
        print("4 - Sair")

        opcao_conta = int(input("Escolha uma opção: "))

        if opcao_conta == 1:
            valor_saque = float(input("Digite o valor do saque: R$ "))

            if valor_saque <= 0:                  
                print("Valor inválido.")
            elif valor_saque > extrato_cliente:
                print("Saldo insuficiente.")
            else:
                extrato_cliente -= valor_saque
                df.loc[index_conta, "extrato"] = extrato_cliente
                df.to_excel("banco_tabajara.xlsx", index=False)

                print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")

        elif opcao_conta == 2:
            valor_deposito = float(input("Digite o valor do depósito: R$ "))

            if valor_deposito <= 0:                
                print("Valor inválido.")
            else:
                extrato_cliente += valor_deposito
                df.loc[index_conta, "extrato"] = extrato_cliente
                df.to_excel("banco_tabajara.xlsx", index=False)
        
                print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")

        elif opcao_conta == 3:
            print(f"Seu saldo atual é: R$ {extrato_cliente:.2f}")

        elif opcao_conta == 4:
            print("Encerrado.")
            break

        else:
            print("Opção inválida.")
