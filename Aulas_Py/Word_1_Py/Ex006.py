# crie um algaritmo que leia um numero e mostre o seu dobro, triplo e a sua raiz quadrada.

x = float(input("Digite um numero"))
a = x*2
b = x*3
c = x ** (1/2)
print("O dobro é = {}".format(a))
print("O triplo é = {}.".format(b))
print("A raiz quadrada dele é = {:.2f}".format(c))
