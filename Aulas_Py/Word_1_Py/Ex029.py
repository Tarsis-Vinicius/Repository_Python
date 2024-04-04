# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km
# acima do limite.
                  #A qual velocidade voce estava na via .
km = float(input("At what speed were you on the road? "))

if km <= 80:
          #Congratulations on driving carefuly   
    print (" Parabens por dirigir com cuidado ")
else:
    multa = (km - 80)* 7
            # Drive more carefully, your fine will be
    print (" Diriga com mais cuidado, sua multa sera de R$35{:.2f}".format(multa))