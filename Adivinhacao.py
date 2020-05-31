import random


def jogar():
    print("*********************************")
    print("Bem vindo no jogo de adivinhação!")
    print("*********************************")

    # numero_secreto = round(random.random() * 100) # mostrado em curso
    # numero_secreto = random.randrange(1,101) # forma alternativa mostrada em curso
    numero_secreto: int = random.randint(1, 100)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nivel de dificuldade? ")
    print("(1) Facil (2) Médio (3) Difícil ")
    nivel = int(input("Define o nível "))

    if (nivel == 0):
        total_de_tentativas = 20
    elif (nivel == 1):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    acertou = False

    # for rodada in range(1, total_de_tentativas, 1)
    # for rodada in [1,2,3,4,5]
    # while (rodada <= total_de_tentativas and acertou != True):
    for rodada in range(1, total_de_tentativas + 1, 1):

        print("Tentativa {} de {}".format(rodada, total_de_tentativas))  # parecido com o strfmt no x++
        # sintaxe alternativa
        # print("Tentativa {0} de {1}".format(rodada, total_de_tentativas))  # parecido com o strfmt no x++

        chute_str = input("Digite um número entre 1 e 100: ")
        # print("o tipo é: ", type(chute_str))
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior = numero_secreto < chute
        menor = numero_secreto > chute

        if (acertou):
            print("Acertou mizeravi, e fez {} pontos".format(pontos))
            break
        else:
            if maior:
                print("Você digitou ", chute, " e por isso errou para cima")
            elif menor:  # else if em outras linguagens
                print("Você digitou ", chute, " e por isso errou para baixo")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    if (acertou == False):
        print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))

    print("Fim do jogo")


if __name__ == '__main__':
    jogar()
