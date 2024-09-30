def dicionario():
    d = {
    "nome" : "Pedro",
    "telefone" : "1234-5678"
}

    d["telefone"] = "9876-5432"

    d["email"] = "blabla@gmail.com"

    return d

def main():
    dicio = dicionario()

    print(dicio)

main()



