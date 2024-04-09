def calcular_prestacao(valor_casa, salario_comprador, anos):
    # Calcula a quantidade de meses
    meses = anos * 12
    
    # Calcula a prestação mensal
    prestacao = valor_casa / meses
    
    # Verifica se a prestação excede 30% do salário
    if prestacao > (salario_comprador * 0.3):
        return False
    else:
        return True

def main():
    # Pede ao usuário para inserir os dados
    valor_casa = float(input("Digite o valor da casa: "))
    salario_comprador = float(input("Digite o salário do comprador: "))
    anos = int(input("Digite em quantos anos ele vai pagar: "))
    
    # Verifica se o empréstimo é aprovado
    if calcular_prestacao(valor_casa, salario_comprador, anos):
        print("Empréstimo aprovado!")
    else:
        print("Empréstimo negado!")

if __name__ == "__main__":
    main()
