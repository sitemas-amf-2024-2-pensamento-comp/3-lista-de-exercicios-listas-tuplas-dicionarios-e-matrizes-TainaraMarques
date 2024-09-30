def sequencia():
    n = 0
    numeros = []
    for n in range(5):
        n = int(input("digite um número: "))
        numeros.append(n)
    
    print (numeros)

    maior = max(numeros)
    print(f"O maior número da sequência é {maior}")
    menor = min(numeros)
    print(f"O menor número da sequência é {menor}")
    return maior,menor
sequencia()