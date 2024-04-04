#Exercício Python 22: Crie um programa que leia o nome
#completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.
x = input('Digite seu nome completo ')
print('Seu nome em letras minusculas fica{}'.format(x.lower()))
print('Seu nome em letras maiusculas fica{}'.format(x.upper()))
print('Seu nome sem espaços fica{}'.format(x.replace(' ','')))
print(len(x.replace(' ','')))