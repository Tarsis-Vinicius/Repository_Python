# Escreva um programa que pergunte a quantidade
# de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = int(input('Por quantos dias você permaneceu com o carro ? '))
km = float(input('Por quantos KM você andou ? '))
r = (d * 60) + (km * 5.93)
print('Permanecendo por {} Dias, e percorrendo {}KM Custará R${}'.format(d, km, r))