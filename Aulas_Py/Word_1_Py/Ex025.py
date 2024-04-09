#  Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
x = input('Qual seu nome completo? ').strip()
print('Existe silva no seu nome ? {}'.format('silva' in x.lower()))