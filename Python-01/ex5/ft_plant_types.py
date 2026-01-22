class Plant:
    """Blueprint of the plant, basic data"""
    def __init__(self, name, height, age):
        """Store the plant info"""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Blueprint of a flower that inherits data from plant (Parent)"""
    def __init__(self, name, height, age, color):
        """Store the flower info"""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Display the flower and it's blooming"""
        print(f"\n{self.name} (Flower): {self.height}cm, {self.age} days,"
              f" {self.color} color")
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """Blueprint of a tree that inherits data from plant (Parent)"""
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        """Store the tree info"""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """Display the Tree and it's shade"""
        print(f"\n{self.name} (Tree): {self.height}cm, {self.age} days,"
              f" {self.trunk_diameter}cm diameter")
        square = 3.14 * ((self.height / 100) ** 2)
        print(f"{self.name} provides {int(square)} square meters of shade")


class Vegetable(Plant):
    """Blueprint of a vegetables that inherits data from plant (Parent)"""
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """Store the vegetable info"""
        super().__init__(name, height, age)
        self.harvest = harvest_season
        self.nutritional = nutritional_value

    def nutrition(self):
        """Display vegetables and its vitamins"""
        print(f"\n{self.name} (Vegetable): {self.height}cm, {self.age} days,"
              f" {self.harvest} harvest")
        print(f"{self.name} is rich in vitamin {self.nutritional}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("tomato", 80, 90, "summer", "C")

    rose.bloom()
    oak.produce_shade()
    tomato.nutrition()
