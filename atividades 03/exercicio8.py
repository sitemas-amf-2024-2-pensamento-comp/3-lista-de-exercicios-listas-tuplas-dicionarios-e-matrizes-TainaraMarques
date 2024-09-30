def pares(n):
    if n % 2 == 0:
        return n
    return None

def impares(n):
    if n % 2 != 0:
        return n
    return None

def main():
    p = []
    i = []
    for n in range(5):
        n = int(input("Digite um número: "))
        par = pares(n)
        impar = impares(n)

        if par is not None:
            p.append(pares(n))
        
        if impar is not None:
            i.append(impares(n))

    print(f"Os pares são {p}")
    print(f"Os impares são {i}")
    return n

main()