# faça um programa que leia a largura e a altura de uma parede em metros, calcule a área
# e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma área de 2M²


x = float(input('qual a altura da parede em metros? '))
y = float(input('qual a largura da parede em metros? '))
z = x * y
a = z / 2
print('Você precisará de {:.2f} Litros de tinta para printar esta parede'.format(a))

