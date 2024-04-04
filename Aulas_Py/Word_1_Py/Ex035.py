
def verificar_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

def main():
    a = float(input("Digite o comprimento da primeira reta: "))
    b = float(input("Digite o comprimento da segunda reta: "))
    c = float(input("Digite o comprimento da terceira reta: "))

    if verificar_triangulo(a, b, c):
        print("As retas podem formar um triângulo.")
    else:
        print("As retas não podem formar um triângulo.")

if __name__ == "__main__":
    main()
