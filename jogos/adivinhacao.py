import random

def jogar():
    print("Bem vindo ao jogo de adivinhação")

    numero_da_sorte=random.randrange(1,101)
    total_tentativas=0
    pontuacao=1000

    try:
        escolha=int(input("Escolha a dificuldade: (1) Fácil | (2) Médio | (3) Difícil: "))

        if(escolha==1):
            total_tentativas=20
        elif(escolha==2):
            total_tentativas=10
        elif(escolha==3):
            total_tentativas=5
        else:
            total_tentativas=10

        for contador in range(1,total_tentativas+1) :
            print(f"Pontuação atual: {pontuacao}")
            print(f"Tentativa {contador} de {total_tentativas}")
            
            try:
                chute=int(input("Digite um número de 1 a 100: "))
            except ValueError:
                print("Valor de escolha deve ser um número válido!")
                continue

            if(chute < 1 or chute > 100):
                print("Número fora do range permitido, tente novamente")
                continue

            acertou = chute==numero_da_sorte
            maior=chute>numero_da_sorte
            menor=chute<numero_da_sorte

            if(acertou):
                print("Parabéns! Você descobriu o número")
                break
            else:
                if(maior):
                    print("Você errou. Seu número é maior do que o número da sorte")
                else:
                    print("Você errou. Seu número é menor do que o número da sorte")    
                pontuacao = pontuacao - abs(numero_da_sorte - chute)
        print(f"Pontuação final: {pontuacao}")
    except ValueError:
        print("Valor de escolha deve ser um número válido!")
        
    print("Fim de Jogo!")

if(__name__ == "__main__"):
    jogar()
