#  contando caracteres
texto01 = "SENAC"
print(texto01[1])
print(texto01[2])

# função len
texto02 = "Inconstituiçãonalicimamente"
print(len(texto02))

# função maiusculo e minusculo
texto03 = "ola mundinho"
print(texto03.upper())

texto04 = "OLA MUNDAÃO"
print(texto04.lower())

print(texto03.capitalize())

texto05 = "python"
print(texto05[0:3])
print(texto05[0:5])

# substituir um texto por outro

texto06 = "Hoje é aula da Heloisa"
novo_texto = texto06.replace("Heloisa da "," do José Milton")
print(novo_texto)

# metodos strings
texto08 = "Pulei carnaval, mas hoje estou estudando"
print("carnaval"in texto08)
# case sensitive = sensivel a letra maiuscula e miniscula

print(texto08.find("estudando"))

# quantas vezes conta a palavra

print(texto08.count("carnaval"))

texto09 = "eu amo java"
print(texto09.startswith("eu"))
print(texto09.endswith("va"))
