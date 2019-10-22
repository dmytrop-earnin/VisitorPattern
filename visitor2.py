
class Vehicle(object):
    def __str__(self):
        return self.__class__.__name__

class Truck(Vehicle):
    def accept(self, visitor):
        visitor.visitTruck(self)
    
class Bus(Vehicle):
    def accept(self, visitor):
        visitor.visitBus(self)

class Suv(Vehicle):
    def accept(self, visitor):
        visitor.visitSuv(self)

class SportCar(Vehicle):
    def accept(self, visitor):
        visitor.visitSportCar(self)

class Repair:
    def visitTruck(self, vehicle):
        print("Repair", vehicle)

    def visitBus(self, vehicle):
        print("Repair", vehicle)

    def visitSuv(self, vehicle):
        print("Repair", vehicle)
 
    def visitSportCar(self, vehicle):
        print("Repair", vehicle)


class Driver:
    def visitTruck(self, vehicle):
        print("Drive", vehicle)

    def visitBus(self, vehicle):
        print("Drive", vehicle)

    def visitSuv(self, vehicle):
        print("Drive", vehicle)

    def visitSportCar(self, vehicle):
        print("Drive", vehicle)


def main():
    vehicles = [Truck(), Bus(), Suv(), SportCar()]
    repair = Repair()
    driver = Driver()
    for v in vehicles:
        v.accept(repair)
        v.accept(driver)

if __name__== "__main__":
    main()