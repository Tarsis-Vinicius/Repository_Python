'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

num = int(input("Enter a number: "))
print('''Choose one of the bases for conversion:
      [ 1 ] Convert to Binary
      [ 2 ] convert to Octal
      [ 3 ] Convert to Hexadecimal''')

option = int(input("Your Choice: "))

if option == 1:
    print('{} Converted to binary equals is a {}'.format(num, bin(num)[2:]))

elif option == 2:
    print('{} Converted to Octal equals is a {}'.format(num, oct(num)[2:]))

elif option == 3:
    print('{} Converted to Hexadecimal equals is a {}'.format(num, hex(num)[2:]))