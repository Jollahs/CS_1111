class Car:
    def __init__(self, color, make, model, fuel_type):
        self.color = color
        self.make = make
        self.model = model
        self.fuel_type = fuel_type

    def __str__(self):
        return self.color + " " + self.model

pauls_car = Car("Silver", "Toyota", "Prius", "Hybrid")
green_car = Car("Green", "Ford", "Mustang", "Gasoline")

print(pauls_car.color)
print(green_car)
