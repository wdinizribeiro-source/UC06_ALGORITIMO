import pandas as pd

print("================================================")
print("        BEM - VINDO AO PORTAL DE ALUNOS")
print("================================================\n")
print("     Digite uma opção no menu")
print("         1 > Criar")
print("         2 > Adicionar")
print("         3 > Apagar")
opcao = int(input("R: "))


if opcao ==1:
    print("Opção 1 selecionada")
    nome = str(input("digite seu nome: "))
    idade = int(input("digite sua idade: "))
    altura = float(input("digite sua altura: "))

    #criação de um dicionario para receber os dados digitados
    dados = {
        "nome": [nome],
        "idade":[idade],
        "altura":[altura]
    }
    excel = pd.DataFrame(dados)
    excel.to_excel("Aula12\Alunos.xlsx", index=False)
    print("Ação finalizada")

elif opcao==2:
    print ("opção 2 selecionada")
    nome = str(input("digite seu nome: "))
    idade = int(input("digite sua idade: "))
    altura = float(input("digite sua altura: "))

    #criação de um dicionario para receber os dados digitados
    dados = {
        "nome": [nome],
        "idade":[idade],
        "altura":[altura]
    }

    leitura_excel = pd.read_excel("Aula12\Alunos.xlsx")
    nova_linha = len(leitura_excel)


    leitura_excel.loc[nova_linha,"nome"] = dados["nome"]
    leitura_excel.loc[nova_linha,"idade"] = dados["idade"]
    leitura_excel.loc[nova_linha,"altura"] = dados["altura"]

# to_excel() serve para criar um anova planilha, pegar os dados digitados pelo usuario em formato
# daframe e gravar os dados na planilha criada

    leitura_excel.to_excel("Aula12\Alunos.xlsx",index=False)
    print("Ação finalizada")

elif opcao==3:
    print("opção 3 selecionada")

    
    linha_apagada = int(input("Digite o numero inteiro: "))
    # ler execel
    leitura_excel = pd.read_excel("Aula12\Alunos.xlsx")
#    apagar um dado 
    leitura_excel = leitura_excel.drop(linha_apagada)
    # salvar execel
    leitura_excel.to_excel("Aula12\Alunos.xlsx",index=False)
    print("Ação finalizada....")