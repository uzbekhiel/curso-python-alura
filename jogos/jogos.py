import adivinhacao
import forca


def escolha_de_jogo():
    try:
        escolha=int(input("Escolha o jogo: (1) Jogo Adivinhação | (2) Jogo da Forca "))
        if(escolha==1):
            adivinhacao.jogar()
        elif(escolha==2):
            forca.jogar()
        else:
            print("Você não escolheu um jogo válido!")
    except ValueError:
        print("Você não escolheu um jogo válido!")

if(__name__ == "__main__"):
    escolha_de_jogo()
