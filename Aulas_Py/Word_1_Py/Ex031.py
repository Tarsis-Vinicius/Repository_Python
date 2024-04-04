""" Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km 
e R$0,45 parta viagens mais longas."""

distancia = float(input(print("What is distance you will travel?")))
if distancia <= 200:
    pay = distancia * 0.5
else:
    pay = distancia * 0.45
print("You're about to start a journey, and you're going to pay R${:.2f}".format(pay))