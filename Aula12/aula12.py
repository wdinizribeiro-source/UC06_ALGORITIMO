import pandas as pd
 
nome = str(input("digite seu nome: "))
idade = int(input("digite sua idade: "))
altura = float(input("digite sua altura: "))
#criação de um dicionario para receber os dados digitados
dados = {
    "nome": [nome],
    "idade":[idade],
    "altura":[altura]
}
# dataframe é a criação do excel em formato que o pandas entende p
# excel = pd.DataFrame(dados)

# to_excel() serve para criar um anova planilha, pegar os dados digitados pelo usuario em formato
# daframe e gravar os dados na planilha criada

# excel.to_excel("Aula12\cadastro.xlsx")
#  loc numero da linha / nome da coluna
# função len => conta quantas linhas existem no excel e cria uma nova linha pra receber
# a nova informaçao do usuario.
leitura_excel = pd.read_excel("Aula12\cadastro.xlsx")
nova_linha = len(leitura_excel)


leitura_excel.loc[nova_linha,"nome"] = dados["nome"]
leitura_excel.loc[nova_linha,"idade"] = dados["idade"]
leitura_excel.loc[nova_linha,"altura"] = dados["altura"]



#print(leitura_excel["nome"])

# apagar linhas de um planilha
leitura_excel = leitura_excel.drop(2)


leitura_excel.loc[1,"nome"] = dados["nome"]
leitura_excel.loc[1,"idade"] = dados["idade"]
leitura_excel.loc[1,"altura"] = dados["altura"]

# salvar
leitura_excel.to_excel("Aula12\cadastro.xlsx", index=False)
