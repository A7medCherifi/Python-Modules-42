class Plant:
    """Blueprint of the plant"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Store the plant info"""
        self.name = name
        self.heigh = height
        self.ages = age

    def grow(self, days: int) -> None:
        """Grow the plant, height and age"""
        for day in range(1, days):
            self.age()
            self.height()

    def age(self) -> None:
        """Grow the plant age"""
        self.ages += 1

    def height(self) -> None:
        """Grow the plant height"""
        self.heigh += 1

    def get_info(self) -> None:
        """Display the plant information"""
        print(f"{self.name}: {self.heigh}cm,"
              f" {self.ages} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    days = 7

    print("=== Day 1 ===")
    rose.get_info()
    rose.grow(days)

    print(f"=== Day {days} ===")
    rose.get_info()

    print(f"Growth this week: +{days - 1}cm")
