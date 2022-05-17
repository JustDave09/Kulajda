import random

class Karta:
    def __init__(self, _hodnota, _barva):
        self.__hodnota = _hodnota
        self.__barva = _barva

    def __str__(self):
        return str(self.__barva) + str(self.__hodnota)

    def vrat_kartu(self):
        """
        Metoda vratí hodnoty karty
        :return: slovník karty
        """
        return [self.__barva, self.__hodnota]

class Balicek:
    def __init__(self):
        self.__karty = []
        barvy = ["S", "K", "P", "L"]
        hodnoty = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

        for barva in barvy:
            for hodnota in hodnoty:
                self.__karty.append(
                    Karta(hodnota, barva)
                )
        self.vypis_balicek()
        self.zamichat()

    def vydat_kartu(self):
        return self.__karty.pop()

    def zamichat(self):
        random.shuffle(self.__karty)

    def vypis_balicek(self):
        for i in self.__karty:
            print(i)

class Hrac:
    def __init__(self, _jmeno):
        self.jmeno = _jmeno
        self.penize = 1000
        self.__ruka = []

    def vezmi_kartu(self, karta):
        self.__ruka.append(karta)

    def ukaz_ruku(self):
        for karta in self.__ruka:
            print(karta)


class Krupier:
    def __init__(self):
        self.__ruka = []

    def lizni(self, balicek, pocet):
        for i in range(pocet):
            self.__ruka.append(balicek.vydat_kartu())

    def rozdej(self, balicek, pocet, hrac):
        for i in range(pocet):
            hrac.vezmi_kartu(balicek.vydat_kartu())

    def ukaz_ruku(self):
        for karta in self.__ruka:
            print(karta)


b1 = Balicek()
h1 = Hrac("David")
k1 = Krupier()

k1.rozdej(b1, 2, h1)
k1.lizni(b1, 2)

print("Dealer:", end=" ")
k1.ukaz_ruku()

print("Hrac:", end=" ")
h1.ukaz_ruku()