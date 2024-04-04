#Como calcular o Seno, cosseno e a tangente de um angulo
import math
x = float(input('Digite um angulo para saber o seno, cosseno e a tangente - '))
x_r = math.radians(x)

s = math.sin(x_r)
print(" O seno de {} é {:.2f}".format(x, s))

c = math.cos(x_r)
print(" O cosseno de {} é {:.2f}".format(x, c))

t = math.tan(x_r)
print(" O seno de {} é {:.2f}".format(x, t))