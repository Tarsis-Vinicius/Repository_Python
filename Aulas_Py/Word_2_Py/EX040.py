'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2)/2

if media < 5:
    print("Infelismente voce foi reprovado")

if media < 5 > 6.9:
    print("Foi por pouco! Voce ainda tem uma chance para recuperar sua nota!")

if media >= 7:
    print("Parabens!! Voce esta aprovado!! <3 <3 <3")