def jogo_da_velha():
    matriz = [
        ["","",""],
        ["","",""],
        ["","",""],
    ]

    matriz[1][1] = "x"

    for linha in matriz:
        print(linha)

jogo_da_velha()