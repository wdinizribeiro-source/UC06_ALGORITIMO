"""
Cria uma lista vazia chamada compras
peça ao usuario pra digitar 3 itens

"""
# criei uma lista 
lista_compra = []
#  pedi usuario ra digitar 3 itens
for  i  in range(3):
    item = input("digite um item:")
    lista_compra.append(item)
    print("sua lista de conpras")
    # mostra toda sua lista no final
    for valor in lista_compra:
        print("-",valor)