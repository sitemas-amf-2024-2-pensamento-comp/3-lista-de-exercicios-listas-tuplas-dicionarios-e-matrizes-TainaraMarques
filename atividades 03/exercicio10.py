def media():
    lista = []
    contN = 0
    n = None
    while True:
        n = int(input("Digite os números a serem adicionados na lista: e digite 0 se desejar parar de adicionar números a lista. "))
        contN += 1
        lista.append(n)

        if n == 0:
            break

    for i in range(len(lista)):
        m = sum(lista) / contN

    print(lista)
    print(m)

media()