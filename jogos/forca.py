import random


def jogar():
    print("Bem vindo ao jogo da Forca")
    
    # Inicializa Variaveis
    acertou = False
    enforcou = False
    chances = 6
    palavra_secreta = pega_palavra_secreta()
    acertos = inicializa_acertos(palavra_secreta)

    while(not acertou and not enforcou):
        print(acertos)
        chute = recebe_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(palavra_secreta, acertos, chute)
        else:
            chances -= 1
            
        acertou = "_" not in acertos
        enforcou = chances == 0

    print(acertos)
    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("Fim de Jogo!")

def marca_chute_correto(palavra_secreta, acertos, chute):
    i = 0
    for letra in palavra_secreta:
        if(chute == letra):
            acertos[i] = letra
        i+=1

def recebe_chute():
    print("Escolha uma letra para tentar acertar a palavra secreta:")
    chute = input("escolha: ")
    return chute

def inicializa_acertos(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def pega_palavra_secreta():
    palavras = []
    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip().lower())
    index = random.randrange(0,len(palavras))
    palavra_secreta = palavras[index]
    return palavra_secreta

if(__name__ == "__main__"):
    jogar()
