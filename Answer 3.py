class Superhero:
    # Constructor to initialize superhero attributes
    def __init__(self, name, alias, superpower, strength_level, home_city, nemesis, is_active=True):
        self.name = name
        self.alias = alias
        self.superpower = superpower
        self.strength_level = strength_level
        self.home_city = home_city
        self.nemesis = nemesis
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

    # Method to add an ally
    def add_ally(self, ally_name):
        if ally_name not in self.allies:
            self.allies.append(ally_name)
            print(f"{ally_name} has been added as an ally!")
        else:
            print(f"{ally_name} is already an ally.")

# Create unique superhero objects
superhero1 = Superhero(
    name="Clark Kent",
    alias="Superman",
    superpower="Flight, Super Strength, Heat Vision",
    strength_level=95,
    home_city="Metropolis",
    nemesis="Lex Luthor"
)

superhero2 = Superhero(
    name="Bruce Wayne",
    alias="Batman",
    superpower="Intelligence, Martial Arts, Gadgets",
    strength_level=85,
    home_city="Gotham City",
    nemesis="Joker"
)

superhero3 = Superhero(
    name="Diana Prince",
    alias="Wonder Woman",
    superpower="Super Strength, Combat Skills, Lasso of Truth",
    strength_level=90,
    home_city="Themyscira",
    nemesis="Ares"
)

# Display details for each superhero
print("\n--- Superhero 1 ---")
superhero1.display_details()

print("\n--- Superhero 2 ---")
superhero2.display_details()

print("\n--- Superhero 3 ---")
superhero3.display_details()

# Add allies
print("\n--- Adding Allies ---")
superhero1.add_ally("Batman")
superhero2.add_ally("Wonder Woman")
superhero3.add_ally("Superman")
