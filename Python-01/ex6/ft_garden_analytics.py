class Plant:
    """Blueprint of a plant"""
    plant_type = "regular"

    def __init__(self, name: str, height: int):
        """Store the plant info"""
        self.name = name
        self.height = height
        self.blooming = False
        self.prize = 0

    def grow(self):
        """Grow the height of plant by 1cm each time"""
        self.height += 1
        print(f"{self.name} grew 1cm")

    def display(self):
        """Display the plant info"""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """Blueprint of a flowering plant that inherits data from plant (Parent)"""
    plant_type = "flowering"

    def __init__(self, name, height, color: str, blooming: bool):
        """Store the plant info"""
        super().__init__(name, height)
        self.color = color
        self.blooming = blooming

    def display(self):
        """Display the info of plant and check if blooming or not"""
        if self.blooming:
            status = "blooming"
        else:
            status = "not blooming"
        plant = super().display()
        return f"{plant}, {self.color} flowers ({status})"


class PrizeFlower(FloweringPlant):
    """Blueprint of a Prize flower that inherits data from flowering plant"""
    plant_type = "prize"

    def __init__(self, name, height, color, blooming, prize: int):
        """Store the plant info"""
        super().__init__(name, height, color, blooming)
        self.prize = prize

    def display(self):
        """Display the info of Prize flower plant"""
        flowering_plant = super().display()
        return f"{flowering_plant}, Prize points: {self.prize}"


class Garden:
    """Create the garden with it's owner"""
    def __init__(self, owner):
        """Store the garden info"""
        self.owner = owner
        self.plants = []
        self.total_growths = 0
        self.blooming_plants = 0
        self.prize = 0
        self.is_grow = 0

    def add_plant(self, plant, display=1):
        """Add plants to the garden and display if the info with some checks"""
        self.plants.append(plant)
        if plant.blooming:
            self.blooming_plants += 1
        if plant.prize > 0:
            self.prize += plant.prize
        if display:
            print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all_plants(self):
        """Grow up all plants of a garden by 1cm"""
        self.is_grow = 1
        for plant in self.plants:
            plant.grow()
            self.total_growths += 1


class GardenManager:
    """Manager of gardens"""
    total_gards = 0
    gards = []

    class GardenStats:
        """Class that do the calculations of the garden manager"""
        def __init__(self, garden):
            """Store the garden data for calculation"""
            self.garden = garden
            self.garden_size = len(garden.plants)
            self.total_growths = garden.total_growths
            self.plants = garden.plants
            self.blooming_plants = garden.blooming_plants
            self.prize = garden.prize
            self.is_grow = garden.is_grow

        def total_plants(self):
            """Return total of plants"""
            return f"Plants added: {self.garden_size}"

        def total_growth(self):
            """Return total growth of plants"""
            return f"Total growth: {self.total_growths}cm"

        def types(self):
            """Calculate how many types of plants are there"""
            prz = flowr = reg = 0
            for plant in self.plants:
                if plant.plant_type == "regular":
                    reg += 1
                elif plant.plant_type == "flowering":
                    flowr += 1
                elif plant.plant_type == "prize":
                    prz += 1
            return f"{reg} regular, {flowr} flowering, {prz} prize flowers"

        def is_valid_height(self) -> bool:
            """Check if the plant height is valid"""
            for plant in self.plants:
                if plant.height <= 0:
                    return False
            return True

        def score_calculator(self, garden):
            """Calculate the total of all plants"""
            score = 0
            prize = self.prize
            blooming = self.blooming_plants
            grows = self.is_grow

            for plant in self.plants:
                score += plant.height

            score += prize + (grows * prize) + (prize * blooming)
            return f"{garden.owner}: {score}"

    @classmethod
    def add_garde(cls, garde):
        """Add new Garden by it's garde"""
        cls.gards.append(garde)
        cls.total_gards += 1

    @staticmethod
    def garden_plants(garden):
        """Display the plants of a garden"""
        for plant in garden.plants:
            print(f"- {plant.display()}")

    @staticmethod
    def total_plants_growth(garden):
        """Display total plants and total growth of plants"""
        stats = GardenManager.GardenStats(garden)
        print(f"\n{stats.total_plants()}, {stats.total_growth()}")

    @staticmethod
    def plant_types(garden):
        """Display how many plants on each type"""
        stats = GardenManager.GardenStats(garden)
        print(f"Plant types: {stats.types()}")

    @staticmethod
    def height_validation(garden):
        """Check if the height is valid and display it"""
        stats = GardenManager.GardenStats(garden)
        print(f"\nHeight validation test: {stats.is_valid_height()}")

    @classmethod
    def create_garden_network(cls):
        """Calculate & Display total height of each garden and total gardens"""
        txt = ""
        for garden in cls.gards:
            if txt != "":
                txt += ", "
            stats = GardenManager.GardenStats(garden)
            txt += f"{stats.score_calculator(garden)}"
        print(f"Garden scores - {txt}")
        print(f"Total gardens managed: {cls.total_gards}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red", True)
    sunflower = PrizeFlower("Sunflower", 50, "yellow", True, 10)

    jasmine = PrizeFlower("Jasmine", 72, "white", True, 10)

    alice = Garden("Alice")
    bob = Garden("Bob")

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    bob.add_plant(jasmine, 0)

    print(f"\n{alice.owner} is helping all plants grow...")
    alice.grow_all_plants()

    GardenManager.add_garde(alice)
    GardenManager.add_garde(bob)

    print(f"\n=== {alice.owner}'s Garden Report ===")
    print("Plants in garden:")
    GardenManager.garden_plants(alice)

    GardenManager.total_plants_growth(alice)
    GardenManager.plant_types(alice)

    GardenManager.height_validation(alice)
    GardenManager.create_garden_network()
