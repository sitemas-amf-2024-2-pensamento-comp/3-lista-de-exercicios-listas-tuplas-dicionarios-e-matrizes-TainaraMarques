def idades():
    pessoas = 0
    idades_dadas = None
    media = 0
    idade = 0
    while idades_dadas != 0:
        idades_dadas = int(input("Digite a sua idade: "))
        pessoas += 1
        idade += idades_dadas
        media = idade/pessoas
    print (media)
    
idades()