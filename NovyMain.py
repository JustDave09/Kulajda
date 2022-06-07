from datetime import datetime, timedelta, date


class Osoba:
    """
    Tato class reprezentuje člověka
    """

    def __init__(self, _jmeno, _narozeni, _email, _telefon):
        self.jmeno = _jmeno
        self.__narozeni = _narozeni
        self.email = _email
        self.telefon = _telefon

    def vypis_jmeno(self):
        return "Jmenuji se " + str(self.jmeno)

    def ziskej_vek(self):
        return 2022 - int(self.__narozeni)


class Ridic(Osoba):
    """
    Tato class reprezentuje ridice
    """

    def __init__(self, _jmeno, _narozeni, _email, _telefon):
        super().__init__(_jmeno, _narozeni, _email, _telefon)


class Policista(Osoba):
    """
    Tato class reprezentuje plicistu
    """

    def __init__(self, _jmeno, _narozeni, _email, _telefon):
        super().__init__(_jmeno, _narozeni, _email, _telefon)
        self.vyplata = None

    def dej_pokutu(self, stanice, pokuta):
        stanice.posli_pokutu(pokuta)


class PolicejniStanice:
    """
    Tato class reprezentuje celý objem databáze policejních záznamů
    """

    def __init__(self, _adresa):
        self.adresa = _adresa
        self.pokuty = []

    def posli_pokutu(self, pokuta):
        self.pokuty.append(pokuta)

    def ziskej_pocet_pokut(self, ridic):
        count = 0
        for pokuta in self.pokuty:
            if pokuta.ridic == ridic:
                count += 1
        return count

    def ziskej_pokuty_stanice(self):
        return len(self.pokuty)

class Pokuta:
    """
    Tato class reprezentuje pokutu
    """

    def __init__(self, _misto, _datum, _cena, _cas_na_zaplaceni, _ridic, _policista):
        # Self udělá v konstruktoru atribut
        self.ridic = _ridic
        self.policista = _policista
        self.misto = _misto
        self.datum = _datum
        self.cena = _cena
        self.cas_na_zaplaceni = _cas_na_zaplaceni

    def datum_zaplaceni(self):
        datum = self.datum + self.cas_na_zaplaceni
        return datum

# ----- Tvoření instancí -----

polda1 = Policista("Jan Novak", 2001, "ahoj@cs.cz", "855 555 205")

zavodnik1 = Ridic("Jan Novak", 2001, "jedu@rychle.cz", "420 420 690")
zavodnik2 = Ridic("Daniel Torreto", 1991, "jedu@rychle.cz", "420 420 690")

stanice = PolicejniStanice("Praha 9")

randomDate1 = date(year=2020, month=1, day=31)
randomDate2 = date(year=2021, month=11, day=30)
randomDate3 = date(year=2022, month=3, day=11)

pokuta1 = Pokuta("Praha9", randomDate1, 2500, timedelta(days=2), zavodnik1, polda1)
pokuta2 = Pokuta("Praha12", randomDate2, 12500, timedelta(days=5), zavodnik1, polda1)
pokuta3 = Pokuta("Praha5", randomDate3, 23500, timedelta(days=8), zavodnik1, polda1)
pokuta4 = Pokuta("Praha8", randomDate2, 23500, timedelta(days=8), zavodnik2, polda1)

# ----- Rozdání pokut -----

polda1.dej_pokutu(stanice, pokuta1)
polda1.dej_pokutu(stanice, pokuta2)
polda1.dej_pokutu(stanice, pokuta3)
polda1.dej_pokutu(stanice, pokuta4)

# ----- Printy -----

print(zavodnik1.vypis_jmeno())
print(zavodnik1.jmeno + " má " + str(stanice.ziskej_pocet_pokut(zavodnik1)) + " pokut")
print("je mu " + str(zavodnik1.ziskej_vek()) + " let")
print("vypršení termínu zaplacení jeho pokuty je " + str(pokuta1.datum_zaplaceni()))

print("\n")

print(zavodnik2.vypis_jmeno())
print(zavodnik2.jmeno + " má " + str(stanice.ziskej_pocet_pokut(zavodnik2)) + " pokut")
print("je mu " + str(zavodnik2.ziskej_vek()) + " let")

print("\n")

print("Stanice drží následující počet pokut:" + str(stanice.ziskej_pokuty_stanice()))