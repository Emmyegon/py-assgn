class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        return "Moving in some way"


class Vehicle:
    
    def __init__(self, name):
        self.name = name
    
    def move(self):
        return "Moving in some way"


# Animal subclasses
class Dog(Animal):
    def move(self):
        return f"{self.name} is running "
    
    def bark(self):
        return "Wooooo woooooo!"


class Bird(Animal):
    def move(self):
        return f"{self.name} is flying "
    
    def sing(self):
        return "Chirp! Chirp!"

# Vehicle subclasses
class Car(Vehicle):
    def move(self):
        return f"{self.name} is driving "
    
    def siren(self):
        return "wiu wiu! wiu wiu!"


class Plane(Vehicle):
    def move(self):
        return f"{self.name} is flying "
    
    def takeoff(self):
        return "Prepare for takeoff!"

# Demonstration
if __name__ == "__main__":
    print(" ANIMALS AND VEHICLES MOVEMENT ")
    print("=" * 40)
    
    # Create animals
    dog = Dog(" Simba")
    bird = Bird("bree")
    
    animals = [dog, bird]
    
    # Create vehicles
    car = Car("Toyota")
    plane = Plane("airways")
    
    vehicles = [car, plane]
    
    # Show how animals move
    print("\n ANIMALS:")
    for animal in animals:
        print(animal.move())
        # Each animal has unique additional methods
        if isinstance(animal, Dog):
            print(animal.bark())
        elif isinstance(animal, Bird):
            print(animal.sing())
        print()
    
    # Show how vehicles move
    print(" VEHICLES:")
    for vehicle in vehicles:
        print(vehicle.move())
        # Each vehicle has unique additional methods
        if isinstance(vehicle, Car):
            print(vehicle.siren())
        elif isinstance(vehicle, Plane):
            print(vehicle.takeoff())
        print()
    
    # Polymorphism demonstration
    print("POLYMORPHISM - SAME METHOD, DIFFERENT BEHAVIOR:")
    
    all_movers = animals + vehicles
    
    for mover in all_movers:
        # Same method call, different results!
        print(mover.move())