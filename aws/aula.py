def Conhecer(nome, cidade):
    print("Oi {}, bom conhecer alguém de {}.".format(nome , cidade))

if __name__ == "__main__":
    nome = input("Qual o seu nome?")
    cidade = input("Onde você mora?")
    Conhecer(nome, cidade)