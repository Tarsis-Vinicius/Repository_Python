# um programa que leia uma frase pelo teclado e mostre quantas
# vezes aparece a letra “A”, em que posição
# ela aparece a primeira vez e em que posição ela aparece a última vez.

x = str(input('Digite uma frase')).upper().strip()
print('A letra -A- aparece {} vezes na frase.'.format(x.count('A')))
print('A primeira letra A apareceu na posição {}'.format(x.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(x.rfind('A')+1))
