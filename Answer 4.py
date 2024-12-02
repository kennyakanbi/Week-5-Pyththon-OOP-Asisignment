class Vehicle:
    """Base class representing a generic vehicle."""
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed  # Speed in km/h

    def display_details(self):
        """Display common details of the vehicle."""
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Speed: {self.speed} km/h")

    def move(self):
        """Placeholder for polymorphism - overridden by subclasses."""
        print(f"The {self.brand} {self.model} is moving.")

    def stop(self):
        """Common method for all vehicles."""
        print(f"The {self.brand} {self.model} has stopped.")


class Car(Vehicle):
    """Subclass representing a car."""
    def __init__(self, brand, model, speed, num_doors):
        super().__init__(brand, model, speed)
        self.num_doors = num_doors

    def display_details(self):
        """Display details specific to a car."""
        super().display_details()
        print(f"Number of Doors: {self.num_doors}")

    def move(self):
        """Override the move method to demonstrate polymorphism."""
        print(f"The car {self.brand} {self.model} is driving on the road.")


class Bike(Vehicle):
    """Subclass representing a bike."""
    def __init__(self, brand, model, speed, type_of_bike):
        super().__init__(brand, model, speed)
        self.type_of_bike = type_of_bike  # e.g., Mountain, Road, Hybrid

    def display_details(self):
        """Display details specific to a bike."""
        super().display_details()
        print(f"Type of Bike: {self.type_of_bike}")

    def move(self):
        """Override the move method to demonstrate polymorphism."""
        print(f"The bike {self.brand} {self.model} is being pedaled.")


# Demonstrate polymorphism
def demonstrate_polymorphism(vehicle):
    """Function to show polymorphic behavior of vehicles."""
    vehicle.display_details()
    vehicle.move()
    vehicle.stop()
    print()


# Example usage
if __name__ == "__main__":
    # Create objects for Car and Bike
    car = Car(brand="Toyota", model="Corolla", speed=180, num_doors=4)
    bike = Bike(brand="Giant", model="Escape 3", speed=25, type_of_bike="Road")

    # Demonstrate polymorphism
    print("--- Car Details and Actions ---")
    demonstrate_polymorphism(car)

    print("--- Bike Details and Actions ---")
    demonstrate_polymorphism(bike)

