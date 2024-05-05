import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem vindo ao jogo de adivinhação feito por gdelacerda23.")
    print("Tente adivinhar o número! (De 0 a 100) ")

    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("O número secreto é maior!")
        elif palpite > numero_secreto:
            print("O número secreto é menor!")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            break

jogo_adivinhacao()

