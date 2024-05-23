def modificar_primeira_letra(frase):
    if frase[0].islower():
        frase = frase[0].upper() + frase[1:]
        return frase, len(frase)

if __name__ == "__main__":
    frase = input("Digite uma frase:")
    frase_modificada, num_caracteres = modificar_primeira_letra(frase)
    print("Frase modificada=", frase_modificada)
    print ("Número de caracteres:", num_caracteres)