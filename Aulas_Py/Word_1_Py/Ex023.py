# Exercício Python 23: Faça um programa que leia um número
# de 0 a 9999 e mostre na tela cada um dos dígitos separados.
x = int(input('informe um numero '))
u = x // 1 % 10
d = x // 10 % 10
c = x // 100 % 10
m = x // 1000 % 10
print('analisando o numero {}'.format(x))
print('Sua unidade é {}'.format(u))
print('Sua dezena é {}'.format(d))
print('Sua centena é {}'.format(c))
print('Sua milhar é {}'.format(m))