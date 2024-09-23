# Car Management System

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def start(self):
        return "The car is on"
    
    def stop(self):
        return "The car is off"
    
    def get_info(self):
        return f"make: {self.make} model: {self.model} year: {self.year}"
    

car1 = Car("Toyota", "camry", 2020)
print(car1.start())
print(car1.stop())
print(car1.get_info())