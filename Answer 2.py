class Superhero:
    def __init__(self, name, alias, superpower, strength_level, home_city, nemesis, is_active=True):
        self.name = name
        self.alias = alias
        self.superpower = superpower
        self.strength_level = strength_level  # Scale of 1 to 100
        self.home_city = home_city  # The superhero's base city
        self.nemesis = nemesis  # The superhero's main enemy
        self.is_active = is_active
        self.missions_completed = 0
        self.allies = []  # List of allies (other superheroes)

    # Method to display superhero details
    def display_details(self):
        print(f"Superhero Details:")
        print(f"Name: {self.name}")
        print(f"Alias: {self.alias}")
        print(f"Superpower: {self.superpower}")
        print(f"Strength Level: {self.strength_level}")
        print(f"Home City: {self.home_city}")
        print(f"Nemesis: {self.nemesis}")
        print(f"Status: {'Active' if self.is_active else 'Retired'}")
        print(f"Missions Completed: {self.missions_completed}")
        print(f"Allies: {', '.join(self.allies) if self.allies else 'None'}")

    # Method to perform a mission
    def perform_mission(self, mission_name):
        if self.is_active:
            print(f"{self.alias} is on a mission: {mission_name}...")
            self.missions_completed += 1
            self.strength_level -= 10  # Decrease strength
            if self.strength_level < 0:
                self.strength_level = 0
            print(f"{self.alias} successfully completed the mission!")
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

    # Method to add an ally
    def add_ally(self, ally_name):
        if ally_name not in self.allies:
            self.allies.append(ally_name)
            print(f"{ally_name} has been added as an ally!")
        else:
            print(f"{ally_name} is already an ally.")

    # Method to fight the nemesis
    def fight_nemesis(self):
        if self.is_active and self.strength_level >= 50:
            print(f"{self.alias} is battling their nemesis, {self.nemesis}!")
            self.strength_level -= 30  # Simulate the toll of battle
            if self.strength_level < 0:
                self.strength_level = 0
            print(f"The battle is over! {self.alias} defeated {self.nemesis}!")
        elif self.strength_level < 50:
            print(f"{self.alias} is too weak to fight {self.nemesis}. Recharge first!")
        else:
            print(f"{self.alias} is retired and cannot fight their nemesis.")

    # Method to retire the superhero
    def retire(self):
        self.is_active = False
        print(f"{self.alias} has retired from superhero duties.")

# Example usage
if __name__ == "__main__":
    # Create a superhero instance
    superhero = Superhero(
        name="Diana Prince",
        alias="Wonder Woman",
        superpower="Super Strength and Combat Skills",
        strength_level=90,
        home_city="Themyscira",
        nemesis="Ares"
    )

    # Display superhero details
    superhero.display_details()

    print("\n--- Adding Allies ---")
    superhero.add_ally("Superman")
    superhero.add_ally("Batman")
    superhero.add_ally("Superman")  # Adding the same ally again

    print("\n--- Performing Missions ---")
    superhero.perform_mission("Rescue civilians from a burning building")
    superhero.perform_mission("Defeat a group of robbers")

    print("\n--- Fighting Nemesis ---")
    superhero.fight_nemesis()

    print("\n--- Recharging Strength ---")
    superhero.recharge(20)

    print("\n--- Retiring the Superhero ---")
    superhero.retire()

    # Attempting actions after retirement
    superhero.perform_mission("Save the city from an alien invasion")
    superhero.fight_nemesis()

    print("\n--- Final Superhero Details ---")
    superhero.display_details()
