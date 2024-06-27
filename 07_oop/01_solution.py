# class Car:
#     brand = None
#     model = None

# car_object = Car()
# print(car_object)

class Car: 
    # Constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car_object = Car("Toyoto", "Foutuner")

print(car_object.brand)
print(car_object.model) 

car_object2 = Car("Tata", "Safari")
print(car_object2.brand)
print(car_object2.model)