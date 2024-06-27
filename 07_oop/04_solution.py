class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return f"{self.__brand}"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
car_object = Car("Toyota", "Corolla")

print(car_object.get_brand())
# print(car_object.full_name())