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

for i in range(len(lista1)):
    for l in range(len(lista2)):
        if lista1[i] == lista2[l]:
            lista3.append(lista1[i])
            break
print(f"\n\nA lista com os iguais foi criada -->> {lista3}")