# faça um programa que leia o preço de um produto e mostre
# um novo valor em liquidação com 5% de desconto

x = float(input('Digite o preço do produto '))
z = x * 0.05
a = x - z
print('Parabêns com o nosso desconto o valor final é de {:.2f}'.format(a))