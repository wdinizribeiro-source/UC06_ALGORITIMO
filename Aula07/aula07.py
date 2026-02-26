#  dicionario em python
aluno  = {
    #  "chave" valor
    "nome_aluno": "Pedro",
    "idade": 19,
    "nota": 8,
    "curso": "tecnico em informatica para Internet",
    "array": [30,True, "texto"],
    "endereço":{
        "cidade":"SP",
        "estado":"SP",
        "numero":234
    }

}

# mostrar dicionario principal
print(aluno["nome_aluno"])
# retorna o nome do aluno
print(aluno["array"])
print(aluno["endereço"])

# acessar apenas um unico campo do endereço
print(aluno["endereço"]["estado"])

# acessando campo especifico de um array
print(aluno["array"][1])

# alterar dados do dicionário
aluno["idade"] = 20
print(aluno["idade"])

# alterar dados dentro de uma array que esta dentro do dicionário
aluno["array"][2] = 9
print(aluno["array"][2])

# altarar dados do dicionario endereço que esta dentro do dicionario aluno

aluno['endereço']["cidade"] = "São paulo"
print(aluno["endereço"]["cidade"])

# adicionar um novo campo
aluno["periodo"] = "periodo noturno"
print(aluno)

# deletar uma informação
del aluno["idade"]
print(aluno)

# percorrer um dicionario usando laço de repetição
for chave in aluno:
    print(chave)

# percorrer um dicionario usando laço de reptição para retornar valores

for valor in aluno.values():
    print(valor)

# percorrer um dicionario e retornar chave e valor
for chave, valor in aluno.items():
    print(chave, ":", valor)