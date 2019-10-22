from __future__ import generators
import random

class Cup(object):
    def accept(self, consumer):
        consumer.visit(self)
    def drink(self, consumer):
        print(self, "Consumed by", consumer)
    def prepare(self, barista):
        print(self, "prepared by", barista)
    def __str__(self):
        return self.__class__.__name__

class SmallCup(Cup): pass
class MediumCup(Cup): pass
class LargeCup(Cup): pass

class Consumer:
    def __str__(self):
        return self.__class__.__name__

class Beverage(Consumer): pass
class Tea(Beverage): pass
class Coffee(Beverage): pass
class Order(Coffee): pass

class CoffeeLover(Coffee):
    def visit(self, cup):
        cup.drink(self)

class TeaLover(Tea):
    def visit(self, cup):
        cup.drink(self)

class Barista(Coffee):
    def visit(self, cup):
        cup.prepare(self)

def main():
    coffeeLover = CoffeeLover()
    teaLover = TeaLover()
    barista = Barista()

    smallCup = SmallCup()
    mediumCup = MediumCup()
    largeCup = LargeCup()

    smallCup.accept(barista)
    smallCup.accept(coffeeLover)
    mediumCup.accept(barista)
    mediumCup.accept(coffeeLover)
    largeCup.accept(teaLover)

if __name__== "__main__":
    main()