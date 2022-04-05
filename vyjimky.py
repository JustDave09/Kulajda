try:
    vstup = int(input())
    a = 3 + vstup
except ValueError:
    print("Cislo tam dej plski")
except Exception as e:
    print("Nastala chyba:")
    print(e)
else:
    print("Všechno OK, pokračuju dale")