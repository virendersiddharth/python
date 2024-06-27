class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
car_object = Car("Toyota", "Corolla")
print(car_object.full_name())