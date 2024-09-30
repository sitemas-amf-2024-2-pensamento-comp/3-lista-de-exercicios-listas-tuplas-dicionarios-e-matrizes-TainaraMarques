def numeros_pares():
    lista = []
    pares = []
    n = None
    while n != 0:
        n = int(input("Digite um número: e digite 0 para sair. "))
        lista.append(n)

        if n % 2 == 0:
            pares.append(n)
    
    print(f"Os pares presentes na lista são {pares}")

numeros_pares()