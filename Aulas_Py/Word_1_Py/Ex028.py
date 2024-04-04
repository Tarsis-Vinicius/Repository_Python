# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número 
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido 
# pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

# Escolhe um número aleatório entre 0 e 5
random_number = random.randint(0, 5)  

# recebe o numero 
resposta = int(input("Enter a number from 0 to 5"))

# verifica se o numero digitado esta certo
if resposta == random_number:
    print("Certa resposta")
else:
    print("Errou!!, tente novamente. O numero escolhido foi... ", random_number)