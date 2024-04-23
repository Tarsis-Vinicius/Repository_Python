"""Crie um programa que faça o computador jogar Jokenpô com você"""

import random

def jogar_jokenpo(escolha_jogador):
    escolhas_possiveis = ['pedra', 'papel', 'tesoura']
    escolha_computador = random.choice(escolhas_possiveis)

    print("Você escolheu:", escolha_jogador)
    print("O computador escolheu:", escolha_computador)

    if escolha_jogador == escolha_computador:
        print("Empate!")
    elif (escolha_jogador == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_jogador == 'papel' and escolha_computador == 'pedra') or \
         (escolha_jogador == 'tesoura' and escolha_computador == 'papel'):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

def main():
    print("Bem-vindo ao Jokenpô!")
    print("Escolha uma opção:")
    print("1. Pedra")
    print("2. Papel")
    print("3. Tesoura")
    escolha = int(input("Digite o número da sua escolha: "))

    if escolha == 1:
        escolha_jogador = 'pedra'
    elif escolha == 2:
        escolha_jogador = 'papel'
    elif escolha == 3:
        escolha_jogador = 'tesoura'
    else:
        print("Escolha inválida. Tente novamente.")
        return

    jogar_jokenpo(escolha_jogador)

if __name__ == "__main__":
    main()

