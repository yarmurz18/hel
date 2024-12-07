class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"Транспортний засіб: {self.brand} {self.model}"


class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def info(self):
        return f"Автомобіль: {self.brand} {self.model}, Кількість дверей: {self.num_doors}"


class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)
        self.bike_type = bike_type

    def info(self):
        return f"Велосипед: {self.brand} {self.model}, Тип: {self.bike_type}"


class Truck(Vehicle):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def info(self):
        return f"Вантажівка: {self.brand} {self.model}, Вантажопідйомність: {self.capacity} тонн"


car1 = Car("Toyota", "Corolla", 4)
car2 = Car("Honda", "Civic", 2)

bike1 = Bike("Giant", "Escape 3", "Міський")
bike2 = Bike("Trek", "Marlin 7", "Гірський")

truck1 = Truck("Volvo", "FH16", 25)
truck2 = Truck("MAN", "TGX", 30)

vehicles = [car1, car2, bike1, bike2, truck1, truck2]

for vehicle in vehicles:
    print(vehicle.info())
