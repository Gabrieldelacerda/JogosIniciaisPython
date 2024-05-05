import random

def escolher_palavra():
    palavras = ["python", "java", "javascript", "ruby", "php", "html", "css"]
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_corretas):
    resultado = ""
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado

def jogar_forca():
    palavra = escolher_palavra()
    letras_corretas = []
    tentativas = 6

    print("Jogo da Forca")
    print("Tente adivinhar:")
    print(mostrar_palavra(palavra, letras_corretas))

    while tentativas > 0:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas:
            print("Você já tentou essa letra.")
            continue

        if letra in palavra:
            letras_corretas.append(letra)
            print("Acertou.")

        else:
            tentativas -= 1
            print("Incorreto, você tem {} tentativas restantes.".format(tentativas))

        print(mostrar_palavra(palavra, letras_corretas))

        if "_" not in mostrar_palavra(palavra, letras_corretas):
            print("Parabéns, você ganhou.")
            break

    if tentativas == 0:
        print("Perdeu! A palavra era", palavra)

if __name__ == "__main__":
    jogar_forca()