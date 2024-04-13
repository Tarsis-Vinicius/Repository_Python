'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

atleta = int(input("Quantos anos voce tem? "))

if atleta <= 7:
    print("Voce esta na categoria MIRIM")

elif atleta < 14:
    print("Voce esta na categoria INFANTIL")

elif atleta  < 19:
    print("Voce esta na categoria JUNIOR")

elif atleta <= 25:
    print("Voce esta na categoria de SENIOR")
    
elif atleta > 25:
    print("Voce esta na categoria de MASTER")
