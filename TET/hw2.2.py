class Warrior:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def show_info(self):
        print(f"Warrior: {self.name}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")

    def got_hit(self, damage):
        print(f"{self.name} got hit by {damage} damage.")
        self.health -= damage
        if self.health < 0:
            self.health = 0

# Test the class
try:
    # Creating a Warrior object
    warrior1 = Warrior(name="Aragorn", health=100, strength=20)

    # Displaying initial info
    print("Initial Information:")
    warrior1.show_info()

    # Warrior got hit
    warrior1.got_hit(30)

    # Displaying updated info
    print("\nUpdated Information:")
    warrior1.show_info()

except ValueError as e:
    print(f"Error: {e}")
