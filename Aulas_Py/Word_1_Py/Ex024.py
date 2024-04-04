# Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
x = input('Qual cidade você mora ? ').strip()
print(x[:5].upper() == 'SANTO')