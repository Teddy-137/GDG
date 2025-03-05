class Vehicle:
    def __init__(self, make, model):
        self._make = make
        self._model = model
    
    @property
    def make(self):
        return self._make
    
    @property
    def model(self):
        return self._model
    
    def describe(self):
        print(f"This is a {self._make} {self._model}")

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self._num_doors = num_doors
    
    @property
    def num_doors(self):
        return self._num_doors
    
    def describe(self):
        print(f"This is a {self.make} {self.model} with {self.num_doors} doors.")

class Bike(Vehicle):
    def describe(self):
        print(f"This is a bike: {self.make} {self.model}")

if __name__ == "__main__":
    my_car = Car("Toyota", "Corolla", 4)
    my_bike = Bike("Yamaha", "R15")
    
    my_car.describe()
    my_bike.describe()
