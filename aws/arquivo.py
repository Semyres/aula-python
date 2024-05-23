'''
Crie uma funcão em python que salve em um arquivo uma frase digitada pelo usuario
'''
# with open("exemplo.txt", "r") as arquivo:
# conteudo = arquivo.read()
# print (contudo)

#def salvar_frase()
#    frase = input("Digite a frase que deseja salvar:")
#arquivo = open("novo.txt", "w")
#arquivo.write("Alterando nosso primeiro arquivo\n")
#arquivo.write("Segunda linha\n")
#arquivo.close()
# for animal in arquivo:
#    print(animal, end="")

#def salvar_frase():
 #   frase = input("Digite a frase que deseja salvar:")
#    arquivo = open("frase.txt", "a")
 #   arquivo.write(frase)
  #  arquivo.close()
   # print("A frase foi salva com sucesso!")
#salvar_frase()

def criarArquivo(texto):
    try:
        with open("arquivo.txt","r+") as arquivo:
            conteudo = arquivo.readlines()
            conteudo.append(texto + "\n")
            arquivo.close()
        arquivo = open("arquivo.txt", "w")
        arquivo.writelines(conteudo)
        arquivo.close()
    except Exception as e:
        print("Falha ao abrir arquivo {}".format(e))