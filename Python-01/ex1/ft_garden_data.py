class Plant:
    """Blueprint of the plant"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Store plant information on it's object"""
        self.name = name
        self.height = height
        self.age = age

    def print_info(self) -> None:
        """Display information about a plant"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")

    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    rose.print_info()
    sunflower.print_info()
    cactus.print_info()
