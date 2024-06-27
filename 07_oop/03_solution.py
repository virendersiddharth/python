class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

class Electric_Car(Car):
    def __init__(self,brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
# car_object = Car("Toyota", "Corolla")
# print(car_object.full_name())
car_object = Electric_Car("Toyota", "Corolla", 90)

print(car_object.brand)
print(car_object.model)
print(car_object.battery_size)
print(car_object.full_name())