import random

def escolher_palavra():
    palavras = ["python", "programacao", "desafio", "computador", "teclado"]
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_corretas):
    palavra_mostrada = ""
    for letra in palavra:
        if letra in letras_corretas:
            palavra_mostrada += letra + " "
        else:
            palavra_mostrada += "_ "
    return palavra_mostrada

def jogo_da_forca():
    palavra = escolher_palavra()
    letras_corretas = []
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")
    print("A palavra possui", len(palavra), "letras.")

    while True:
        print("\nPalavra:", mostrar_palavra(palavra, letras_corretas))
        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas:
            print("Você já tentou esta letra. Tente novamente.")
            continue

        if letra in palavra:
            letras_corretas.append(letra)
            if len(set(letras_corretas)) == len(set(palavra)):
                print("\nParabéns, você ganhou! A palavra era:", palavra)
                break
        else:
            tentativas -= 1
            print("Letra errada. Você tem", tentativas, "tentativas restantes.")

        if tentativas == 0:
            print("\nGame Over! A palavra era:", palavra)
            break

jogo_da_forca()
