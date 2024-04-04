# Faça um programa que leia o nome completo de uma pessoa, mostrando em
# seguida o primeiro e o último nome separadamente.

# Lê o nome completo da pessoa
nome_completo = input("Digite seu nome completo: ")

# "split" Divide o nome completo em partes separadas pelo espaço em branco
partes_do_nome = nome_completo.split()

# Obtém o primeiro nome (primeiro elemento da lista)
primeiro_nome = partes_do_nome[0]

# Obtém o último nome (último elemento da lista)
ultimo_nome = partes_do_nome[-1]

# Exibe o primeiro e o último nome separadamente
print("Primeiro nome:", primeiro_nome)
print("Último nome:", ultimo_nome)