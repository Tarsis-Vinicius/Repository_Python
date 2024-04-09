# O mesmo professor do desafio 19 quer sortear a ordem de
# apresentação de trabalhos dos alunos. Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

a1 = input('nome do primeiro aluno -')
a2 = input('nome do segundo aluno -')
a3 = input('nome do terceiro aluno -')
a4 = input('nome do quarto aluno -')

alunos = [a1, a2, a3, a4]
shuffle(alunos)
print('A ordem sorteada foi: ', alunos)