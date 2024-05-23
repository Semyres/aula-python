import arquivo, os

arquivo = arquivo
sair = False

while sair == False:
    opcao = input("Escolha uma opção:\n"
                    "1: Cadastrar item\n"
                    "2: Listar itens\n"
                    "3: Sair\n")
    if opcao == "1":
        item = input("Digite o item a ser adicionado:")
        arquivo.criarArquivo(item)
        os.system('cls')
    elif opcao =="2":
        with open("arquivo.txt", "r") as arquivo:
            conteudo = arquivo.read()
        os.system('cls')
        for item in conteudo:
            print(item, end="")
        #print("Falta implementar")
    elif opcao == "3":
        sair = True
    else:
        print("Opção inválida")