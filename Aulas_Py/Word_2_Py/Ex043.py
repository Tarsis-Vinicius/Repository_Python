'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''

altura = float(input("Para falarmos o seu IMC precisaremos da sua altura e do seu peso, tudo bem? Nos diga a sua altura primeiro: "))
peso = float(input("Muito bem! Agora qual seu peso em Kg? "))
imc = peso/ (altura **2)


if imc < 18.5:
    print("Seu IMC e de {:.1f}. Voce esta abaixo do peso".format(imc))

elif 18.5 < imc <= 25:
    print("Seu IMC é de {:.1f}. Você está em seu peso ideal.".format(imc))

elif 25 < imc <= 30:
    print("Seu IMC é de {:.1f}. Você está com sobrepeso.".format(imc))

elif 30 < imc <= 40:
    print("Seu IMC é de {:.1f}. Cuidado! Você está com obesidade.".format(imc))

elif imc > 40:
    print("Seu IMC é de {:.1f}. Cuidado! Você está com obesidade mórbida.".format(imc))