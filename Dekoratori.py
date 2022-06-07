import math

prase = "Ahoj"

"""
def ahoj_dane(func):
    func(data)
    print("Udělal jsem tuto funkci :point_UP:")


@ahoj_dane
def dave(data):
    print("Dave " + str(data))



@ahoj_dane
def vyuziva_iq():
    print("Používá IQ")
    print("Matouše a Dana")

C = 5
D = 2


def filter(func):
    def wrapper_filter(*args, **kwargs):
        data = func(*args, **kwargs)
        data = round(data)
        return data

    print("Výsledné číslo po zaokrouhlení je: " + str(wrapper_filter))


def nasobeni(A, B):
    return A * B


@filter
def deleni(A, B):
    return A / B


deleni(5, 2)

# print(deleni(A,B))
"""


class Person:
    def __init__(self):
        self.__money = 0

    def set_money(self, amount):
        self.__money += amount

    def get_money(self):
        return self.__money


p1 = Person()
p1.set_money(100)
p1.get_money()


class Persona:
    def __init__(self):
        self.__money = 0

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, amount):
        if amount > 0:
            self.__money += amount


p2 = Persona()
p2.money = 100
print(p2.money)
