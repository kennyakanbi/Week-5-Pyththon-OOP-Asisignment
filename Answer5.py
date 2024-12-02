class Vehicle:
    """Base class for all vehicles."""
    def __init__(self, name):
        self.name = name

    def move(self):
        """Common action for all vehicles, to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement the move() method")

    def display(self):
        """Display the name of the vehicle."""
        print(f"This is a {self.name}.")


class Car(Vehicle):
    """Subclass representing a car."""
    def move(self):
        print(f"The {self.name} is driving on the road. 🚗")


class Plane(Vehicle):
    """Subclass representing a plane."""
    def move(self):
        print(f"The {self.name} is flying in the sky. ✈️")


class Boat(Vehicle):
    """Subclass representing a boat."""
    def move(self):
        print(f"The {self.name} is sailing on the water. 🚤")


# Demonstrate polymorphism
def demonstrate_vehicle_movement(vehicle):
    """Function to demonstrate polymorphism with the move() method."""
    vehicle.display()
    vehicle.move()
    print()


# Example usage
if __name__ == "__main__":
    # Create vehicle objects
    car = Car(name="Toyota Corolla")
    plane = Plane(name="Boeing 747")
    boat = Boat(name="Titanic")

    # Demonstrate movement for each vehicle
    print("--- Car Movement ---")
    demonstrate_vehicle_movement(car)

    print("--- Plane Movement ---")
    demonstrate_vehicle_movement(plane)

    print("--- Boat Movement ---")
    demonstrate_vehicle_movement(boat)

