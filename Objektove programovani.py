#UML ---- CLASS DIAGRAM

# --- Třídy ---

# názvy tříd začínají velkým písmenem
# u atributů je data type
# metody mají také data type, který vrací

# Každá třída musí mít komentář co v ní je a co representuje

# --- Vazby ---

# kardinality ukazují kolik jiných tříd má třída

# existují dědící vazby (`profesor` a `student` mají atributy "člověka")


# (o .o )

class Person:
    """
    Tato class reprezentuje člověka
    """
    # Konstruktor __init__ tvoří instanci třídy podle své potřeby-
    def __init__(self, _name, _birth, _email):
        # Self udělá v konstruktoru atribut
        self.name = _name
        # __ před názvem self atributu vytvoříme "skrytý atribut" (veliké bezpečnostní záležitosti)
        self.__birth = _birth
        self.email = _email
        self.__adress = None

    def __str__(self):
        return "Hello I am " + self.name

    def purchase_parking_pass(self):
        print("Parking purchased!")

    def get_age(self):
        print(2022 - self.__birth)

    def set_adress(self, _adress):
        self.__adress = _adress

    def get_adress(self):
        return self.__adress

# Takto se dědí
class Professor(Person):
    """
    Tato class reprezentuje učitele v naší škole
    """
    def parking_with_discount(self):
        print("Parking purchased with discount for " + str(self.name))

class Student(Person):
    """
    Tato class reprezentuje žáka ve škole
    """
    def __init__(self, _name, _birth, _email, _debt):
        super(). __init__(_name, _birth, _email)
        self.loan = _debt

    def pay_debts(self):
        print("I don't have enought money to pay my own debts :(")

class Adress:
    """
    Tato class reprezentuje adresu
    """
    def __init__(self, _street, _city, _house_number):
        self.street = _street
        self.city = _city
        self.house_number = _house_number

    def __str__(self):
        return "The location is at" + self.city + ", " + self.street + ", " + str(self.house_number)

    def get_location(self):
        print("This building is located at " + str(self.city) + " at street " + str(self.street) + " house number " + str(self.house_number))

# ===============================================================

peter = Person("Peter Parker", 1900, "ahoj@oka.lol")
peter.purchase_parking_pass()
peter.get_age()
print("----------------")

jack = Student("Jack Sparrow", 2004, "zak@skoly.cz", 500)
jack.pay_debts()
jack.get_age()

print("----------------")
luke = Professor("Luke Walker", 1989, "walker@skoly.cz")
luke.parking_with_discount()

print("----------------")
school = Adress("Letovická", "Brno", 206)
school.get_location()

print("----------------")
peter.set_adress(school)
print(peter.get_adress())
#luke._Person__adress=school