#Superhero Class in Python
class Superhero:
    # Constructor to initialize superhero attributes
    def __init__(self, name, alias, superpower, strength_level, is_active=True):
        self.name = name
        self.alias = alias
        self.superpower = superpower
        self.strength_level = strength_level  # Scale of 1 to 100
        self.is_active = is_active  # True if the superhero is active, False otherwise
        self.missions_completed = 0

    # Method to display superhero details
    def display_details(self):
        print(f"Superhero Details:")
        print(f"Name: {self.name}")
        print(f"Alias: {self.alias}")
        print(f"Superpower: {self.superpower}")
        print(f"Strength Level: {self.strength_level}")
        print(f"Status: {'Active' if self.is_active else 'Retired'}")
        print(f"Missions Completed: {self.missions_completed}")

    # Method to perform a mission
    def perform_mission(self):
        if self.is_active:
            self.missions_completed += 1
            self.strength_level -= 5  # Simulate energy depletion
            if self.strength_level < 0:
                self.strength_level = 0
            print(f"{self.alias} successfully completed a mission! Missions completed: {self.missions_completed}")
        else:
            print(f"{self.alias} is retired and cannot perform missions.")

    # Method to recharge strength
    def recharge(self, amount):
        if self.is_active:
            self.strength_level += amount
            if self.strength_level > 100:
                self.strength_level = 100
            print(f"{self.alias} has recharged. Strength level is now {self.strength_level}.")
        else:
            print(f"{self.alias} is retired and cannot recharge.")

    # Method to retire the superhero
    def retire(self):
        self.is_active = False
        print(f"{self.alias} has retired from superhero duties.")

# Example usage
if __name__ == "__main__":
    # Create a superhero instance
    superhero = Superhero(name="Bruce Wayne", alias="Batman", superpower="Intelligence and Gadgets", strength_level=85)

    # Display superhero details
    superhero.display_details()

    print("\n--- Performing Missions ---")
    # Perform some missions
    superhero.perform_mission()
    superhero.perform_mission()

    print("\n--- Recharging Strength ---")
    # Recharge strength
    superhero.recharge(20)

    print("\n--- Retiring the Superhero ---")
    # Retire the superhero
    superhero.retire()

    # Try to perform another mission after retirement
    superhero.perform_mission()

    print("\n--- Final Superhero Details ---")
