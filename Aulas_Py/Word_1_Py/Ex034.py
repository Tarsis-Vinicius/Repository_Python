'''
Escreva um programa que pergunte o salário de um funcionário e 
calcule o valor do seu aumento. Para salários superiores a R$1250,00,
calcule um aumento de 10%. Para os inferiores ou iguais, o aumento 
é de 15%
'''

salary = float(input("What is your salary today? "))
if salary > 1250:
    new_salary = salary + (salary * 10/100)
    print("Congratulations, your salary now is {} ".format(new_salary))
else:
    new_salary = salary + (salary * 15/100)
    print("Congratulations, your salary now is R${:.2f} ".format(new_salary))    