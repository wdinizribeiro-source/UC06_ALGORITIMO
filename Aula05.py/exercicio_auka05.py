entrada = input("digite um numero inteiro: ").strip()
print("Você digitou (texto):", entrada)

if entrada.isdigit():
    print("é um numero inteiro válido")
    um_numero = int(entrada)  
else:
    print("Inválido: tente novamente")
    while True:
        entrada = input("digite um numero inteiro: ").strip()
        if entrada.isdigit():
            um_numero = int(entrada)
            break
        else:
            print("tente novamente")  


print(f"\nTabuada de {um_numero}:")
for i in range(1, 11):
    print(f"{um_numero} x {i:2} = {um_numero * i}")