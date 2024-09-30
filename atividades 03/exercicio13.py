def fibonacci():
    n = int(input("Digite um número: "))
    f = [0, 1]
    mult = 0
    while len(f) < n:
        mult = f[-1] + f[-2]
        f.append(mult)

    print(f)

fibonacci()