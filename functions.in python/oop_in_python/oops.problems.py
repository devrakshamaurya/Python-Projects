#Basic Class and Object
#create a car class with attributes like brand and model. then create an instance of this class.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata", "Safari")
print(my_new_car.model)

#my_car (object),, #Car (class)


#Class Method and self
#Add a method to the car class that displays the full name of the car (brand and model)

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    

my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())


my_new_car = Car("Tata", "Safari")
print(my_new_car.model)


#Inheritance
# create an electriccar class that inherits from the car class and has an additional attribute battery_size

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)    
        self.battery_size = battery_size 

my_tesla = ElectricCar("Tesla", "Model S", "85Kwh")
print(my_tesla.full_name())


#Encapsulation
#modify the car class to encapsulate the brad attribute , making it private and providea getter method for it.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self): 
        return self.__brand + " !"   
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)    
        self.battery_size = battery_size 

my_tesla = ElectricCar("Tesla", "Model S", "85Kwh")
#print(my_tesla.brand)
print(my_tesla.get_brand())





