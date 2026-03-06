# abrir o arquivo
#open("nota.txt","w")

#  abrir o arquivo e digitar informações o as siginifica como
with open("aula10/nota.txt", "w") as nota_aluno:
    nota_aluno.write("Ola Mundo")

# pede pra abrir e ler o arquivo
with open("aula10/nota.txt","r") as leitura_arquivo:
    recebe_texto=leitura_arquivo.read()
    print(recebe_texto)

#  adcionar um textoao final do arquivo
with open("aula10/nota.txt","a") as adiciona_novo_texto:
    adiciona_novo_texto.write("\n aqui tem um novo texto")