
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
        print("Jmenuji se " + str(self.jmeno))

    def ziskej_vek(self):
        print(2022 - int(self.__narozeni))


class Ridic(Osoba):
    """
    Tato class reprezentuje ridice
    """

    def __init__(self, _jmeno, _narozeni, _email, _telefon, _vyplata):
        super().__init__(_jmeno, _narozeni, _email, _telefon)
        self.vyplata = _vyplata
        self.pokuty = []

    def ziskej_pocet_pokut(self):
        return len(self.pokuty)

    def vezmi_pokutu(self, pokuta):
        self.pokuty.append(pokuta)


class Policista(Osoba):
    """
    Tato class reprezentuje plicistu
    """

    def __init__(self, _jmeno, _narozeni, _email, _telefon, _pocet_aut):
        super().__init__(_jmeno, _narozeni, _email, _telefon)
        self.pocet_aut = _pocet_aut
        self.vyplata = None

    def dej_pokutu(self, ridic, misto, datum, cena, cas_na_zaplaceni):
        ridic.vezmi_pokutu(Pokuta(misto, datum, cena, cas_na_zaplaceni))


class Pokuta:
    """
    Tato class reprezentuje pokutu
    """

    def __init__(self, _misto, _datum, _cena, _cas_na_zaplaceni):
        # Self udělá v konstruktoru atribut
        self.misto = _misto
        self.datum = _datum
        self.cena = _cena
        self.cas_na_zaplaceni = _cas_na_zaplaceni

    def nejpozdejsi_datum_zaplaceni(self):
        pass

polda1 = Policista("Jan Novak", 2001, "ahoj@cs.cz", "855 555 205")
