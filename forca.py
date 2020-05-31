import random


def msg_inicio():
    print("*********************************")
    print("***Bem vindo no jogo de forca!***")
    print("*********************************")


def set_secret_word(file_path):
    palavras = []
    with open(file_path, "r") as arquivo:  # mesma logica do using no c#
        for line in arquivo:
            palavras.append(line.strip().upper())

        arquivo.close()
    return palavras


def find_secret_word_in_list(file_path="D:\Python_CodesSaved\FileStream\palavras.txt", primeira_linha_valida=0):
    palavras = set_secret_word(file_path=file_path)
    return palavras[random.randrange(primeira_linha_valida, len(palavras))]


def init_letras_acertadas(palavra_secreta):
    # Listas são declaradas com [] enquanto tuples são declarados com ()
    # a diferença de ambos é que o tuple é imutavel enquanto a lista nao
    return ["_" for letra in palavra_secreta]
    # inicia a lista com _ para letra da palavra secreta
    # o nome disso é List Comprehensions


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def the_game(palavra_secreta):
    letras_acertadas = init_letras_acertadas(palavra_secreta)

    erros = 0
    enforcou = False
    acertou = False

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = pede_chute()

        erro_atual = valida_e_marca_chute(chute, palavra_secreta, letras_acertadas)
        if (erro_atual > 0):
            erros += 1

        desenha_forca(erros)
        acertou = "_" not in letras_acertadas
        enforcou = erros >= 7

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


def pede_chute():
    return input("Qual letra: ").strip().upper()


def marca_chute(chute, palavra_secreta, letras_acertadas):
    index = 0

    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra

        index += 1


def valida_e_marca_chute(chute, palavra_secreta, letras_acertadas):
    ret = 0

    if (chute in palavra_secreta):
        marca_chute(chute, palavra_secreta, letras_acertadas)
    else:
        ret = 1

    return ret


def jogar():
    msg_inicio()

    palavra_secreta = find_secret_word_in_list()

    the_game(palavra_secreta)


if __name__ == '__main__':
    jogar()
