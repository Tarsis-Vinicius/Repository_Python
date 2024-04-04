
from datetime import date
ano = int(input("What year do you want to analyze? If you want to know the current year, enter 0 "))
if ano == 0:    
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("The year {} is a leap year".format(ano))
else:
    print("The year {} is not a leap year".format(ano))