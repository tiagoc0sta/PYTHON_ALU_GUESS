import random

print("******************************************")
print("*****Bem vindo ao jodo de adivinhação!****")
print("******************************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos = 100

print("Qual nível de dificuldade? ", numero_secreto)
print("(1) Fácil (2) Médio (3) Dificil" )

nivel = int(input("Defina o nível: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

print(numero_secreto)


for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um numero entre 1 e 100: ")
    print("Voce digitou ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Voce deve digitar um numero entre 1 e 100!")
        continue


    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Voce acertou e fez {} pontos!".format(pontos))
        break
    else:
        if(maior):
            print("Voce errou! O seu chute foi maior do que o numero secreto.")
        elif (chute < numero_secreto):
            print("Voce errou! O seu chute foi menor do que o numero secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos


print("Fim do jogo")