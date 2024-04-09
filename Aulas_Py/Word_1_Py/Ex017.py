#calcule a hipotenusa de um triangulo
import math
x = float(input('Digite o valor do cateto oposto - '))
y = float(input('Digite o valor do cateto adjacente - '))
r = math.hypot(x, y)
print('A hipotenusa vale {:.2f}'.format(r))