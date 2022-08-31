import random

FORCAIMG = ['''

    +----+
         |
         |
         |
         |
         |
=============''', '''

    +----+
    |    |
    O    |
         |
         |
         |
=============''', '''

    +----+
    |    |
    O    |
    |    |
         |
         |
=============''', '''

    +----+
    |    |
    O    |
   /|    |
         |
         |
=============''', '''

    +----+
    |    |
    O    |
   /|\   |
         |
         |
=============''', '''

    +----+
    |    |
    O    |
   /|\   |
   /     |
         |
=============''', '''

    +----+
    |    |
    O    |
   /|\   |
   / \   |
         |
=============''']

palavras = 'banana telescópio cachorro gato girafa hamburg pizza alimentos biscoito carne supermercado pai mãe'.split()

"""
Função Principal
"""


def main():
    global FORCAIMG
    print('F O R C A')
    letrasErradas = ''
    letrasAcertadas = ''
    palavraSecreta = geraPlavraAleatória().upper()
    jogando = True

    while jogando:
        imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta)
        palpite = recebePalpite(letrasErradas + letrasAcertadas)
        if palpite in palavraSecreta:
            letrasAcertadas += palpite
            if verificaSeGanhou(palavraSecreta, letrasAcertadas):
                print("Exato! A palavra secreta é " + palavraSecreta + '! Você ganhou')
                jogando = False

        else:
            letrasErradas += palpite
            if len(letrasErradas) == len(FORCAIMG) - 1:
                imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta)
                print("Você excedeu o limite de palpites!!")
                print("Depois de " + str(len(letrasErradas)) + ' letras erradas e ' + str(len(letrasAcertadas)), end=' ')
                print("Letras corretas, a palavra era " + palavraSecreta + '.')
                jogando = False

        if not jogando:
            if jogarNovamente():
                letrasErradas = ''
                letrasAcertadas = ''
                jogando = True
                palavraSecreta = geraPlavraAleatória().upper()


"""
Função que retorna uma string a partir da lista de palavras global
"""


def geraPlavraAleatória():
    global palavras
    return random.choice(palavras)


"""
Recebe uma string palavra ou lista e imprime essa com
espaço entre suas letras ou string's
"""


def imprimeComEspaços(palavra):
    for letra in palavra:
        print(letra, end='')
    print()


"""
feito a partir da variável global que contem as imagens
do jogo em ASCII art, e também as letras chutadas de maneira
correta e as letras erradas e a palavra secreta
"""


def imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta):
    global FORCAIMG
    print(FORCAIMG[len(letrasErradas)] + '\n')

    print("Letras erradas: ", end=' ')
    imprimeComEspaços(letrasErradas)

    vazio = '_' * len(palavraSecreta)

    for i in range(len(palavraSecreta)):
        if palavraSecreta[i] in letrasAcertadas:
            vazio = vazio[:i] + palavraSecreta[i] + vazio[i + 1:]

    imprimeComEspaços(vazio)


"""
Função feita para garantir que o usuário coloque uma
entrada valida, ou seja, que seja uma única letra
que ele ainda não tenha chutado
"""


def recebePalpite(palpitesFeitos):
    while True:
        print()
        palpite = input("Diga uma letra. \n").upper()

        if len(palpite) != 1:
            print("Coloque uma única letra! \n")
        elif palpite in palpitesFeitos:
            print("Essa letra já existe. Digite outra letra! \n")
        elif not 'A' <= palpite <= 'Z':
            print("Insira apenas letras! \n")
        else:
            return palpite


"""
função que pede para o usuário decidir se ele quer
jogar novamente e retorna um booleano representando
a resposta
"""


# O comando ".startswith()" consegue capturar o primeiro caracter de uma string.
def jogarNovamente():
    return input("Você quer jogar novamente? (Sim ou Não) \n").upper().startswith('S')


"""
Função que verifica se o usuário acertou todas as
letras da palavra secreta
"""


def verificaSeGanhou(palavraSecreta, letrasAcertadas):
    ganhou = True
    for letra in palavraSecreta:
        if letra not in letrasAcertadas:
            ganhou = False
            break
    return ganhou


main()