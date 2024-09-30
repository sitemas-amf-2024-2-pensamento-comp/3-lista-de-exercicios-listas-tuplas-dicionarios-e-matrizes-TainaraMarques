def contar_elemento():
    lista = []
    cont_elemento = 0
    while True:
        n = int(input("Digite os elementos da lista: "))
        lista.append(n)

        if n == 0:
            break

    elemento = 7
    for i in range(len(lista)):
        if lista[i] == elemento:
            cont_elemento += 1
    print (f"A quantidade de vezes em que o elemento aparece na lista é: {cont_elemento}")
    print(f"O elemento era {elemento}")
    return elemento

contar_elemento()