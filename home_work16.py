class Car:
    def __init__(self, year, manufacturer, model, fuel_consumption):
        self.year = year
        self.manufacturer = manufacturer
        self.model = model
        self.mileage = 0
        self.fuel_consumption = fuel_consumption

    def drive(self):
        print(f"Я авто марки {self.model}, їду по справам господаря")

    @property
    def cost_of_service(self):
        return self.mileage * 7.6  


car1 = Car(2020, "Toyota", "Corolla", 6.5)
car2 = Car(2018, "Ford", "Focus", 7.2)
car3 = Car(2021, "Tesla", "Model 3", 0.0)

car1.mileage = 15000

print(f"Вартість обслуговування {car1.model}: {car1.cost_of_service:.2f} одиниць")

car2.drive()
