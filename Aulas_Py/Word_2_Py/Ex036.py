'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

valor_casa = float(input("What's the value of the house? "))
valor_salario = float(input("What's your salary? "))
anos = int(input("How many years do you want to pay? "))

valor_parcelas = valor_casa / (anos * 12)

limite = valor_salario * 0.3

if valor_parcelas <= limite:
    print("Congratulations your credit is approved")
else:
    print("Unfortunately, you didn't pass.")