class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"

class Electric_Car(Car):
    def __init__(self,brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"
    

tesla = Electric_Car("Tesla", "Model s", "85kwh")
print(tesla.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())