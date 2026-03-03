"""
dicionario  são {} -> Para acessar dados usamos o nome da chave
listas  são [] -> Para acessar dados usamos a posição da lista
"""
notas = [10,8,5,10,True, 4,7,2]

# adcionar um dado na ultima posição
# notas.append("SENAC")
# print(notas)


#  adicionar um dados na posição desejada
# notas.insert(0, False)
# print(notas)

#  mesclar duas listas e formar somente uma 
# novalista = ["ola mundo", 1980,24.7]
# novalista.extend(notas)
# print(novalista)


# removendo um dado
notas.remove(10)
print(notas)

notas.remove(True)
print(notas)

# remove um dado pelo indice (ultimo)
nomes_numeros = [390,"Adenilson", 19, "Anna", 45, "Iara", 390, 390]
nomes_numeros.pop(2)
print(nomes_numeros)

# limpa toda sua lista
# print(nomes_numeros.clear())

# retornar a posição do dado
print(nomes_numeros.index(390))
print(nomes_numeros)

# conta ocorrencias: no caso abaixo a quantidade de vezes que aparece "390"
print(nomes_numeros.count(390))

# ordena a lista de forma crescente (não a aleatoria )

numeros = [34, 45, 67, 89, 43, 44, 26, 58, 66 , 33, 90]
numeros.sort()
print(numeros)

nomes = ["Adenilson", "Anna", "Beatriz", "wellington"]
nomes.sort()
print(nomes)

# inverte a ordem decrescente 
numeros.reverse()
print(numeros)

nomes.reverse()
print(nomes)