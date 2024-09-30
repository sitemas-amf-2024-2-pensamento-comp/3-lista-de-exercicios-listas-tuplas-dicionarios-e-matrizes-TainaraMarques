lista1 = []
lista2 = []
lista3 = []
n1 = 0
cont1 = 0
cont2 = 0

while cont1 <= 4:
    n1 = int(input("Digite um numero para preencher a primeira lista: "))
    cont1 += 1
    lista1.append(n1)

while cont2 <= 4:
    n2 = int(input("Digite os números da segunda sequência: "))
    cont2 += 1
    lista2.append(n2)

for i in range (len(lista1)):
    lista3.append(lista1[i])
    for i in range(len(lista2)):
        if lista2[i] not in lista3:
            lista3.append(lista2[i])



print(f"\n\nEstá foi a lista criada com os valores informados -->> {lista3}\n\n")
