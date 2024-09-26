# Employee management system

class Employee:
    def __init__(self, name, id_number, salary):
        self.name = name
        self.id_number = id_number
        self.salary = salary
        
    def give_raise(self):
        amount = float(input("Enter the percentage increase in the salary: "))
        self.salary *= amount
        return f"The raise is: {self.salary}"
    
    def display_info(self):
        return f"Name: {self.name} Id_number: {self.id_number} salary: {self.salary}"
    
    
employee = Employee(input("Enter employee name: "), int(input("Enter Employee Id_number: ")) ,float(input("Enter the salary: ")), )

employee.give_raise()

employee.display_info()