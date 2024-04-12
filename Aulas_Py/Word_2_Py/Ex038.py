'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais'''

num_a = int(input("Escreva um numero: "))
num_b = int(input("Escreva outro numero: "))

if num_a > num_b:
    print("O primeiro valor e maior")
elif num_a < num_b:
    print("O segundo valor e maior")
elif num_a == num_b:
    print("Não existe valor maior, os dois são iguais")