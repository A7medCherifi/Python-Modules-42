class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class Plant:
    def __init__(self, name: str, water: int, sunlight: int) -> None:
        self.name = name
        self.water = water
        self.sun = sunlight


class GardenManager:
    tank = 5

    def __init__(self) -> None:
        self.plants = []

    def add_plants(self, plant: object) -> None:
        try:
            if not plant.name:
                raise PlantError("Plant name cannot be empty!")
            if plant.water < 0 or plant.sun < 0:
                raise PlantError("Invalid input!")

            self.plants.append(plant)
            print(f"Added {plant.name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}\n")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                if GardenManager.tank <= 0:
                    raise WaterError("tank is empty!")
                plant.water += 2
                GardenManager.tank -= 2
                print(f"Watering {plant.name} - success")
        except WaterError as e:
            print(f"Error watering plant: {e}")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_plants_health(self) -> None:
        try:
            for plant in self.plants:
                if plant.water > 10:
                    raise WaterError(f"Error checking {plant.name}: Water le"
                                     f"vel {plant.water} is too high (max 10)")
                if plant.sun > 12:
                    raise PlantError(f"Error checking {plant.name}: Sunlight "
                                     f"hours {plant.sun} is too high (max 12)")
                print(f"{plant.name}: healthy (water: {plant.water}, "
                      f"sun: {plant.sun})")

        except (WaterError, PlantError) as e:
            print(f"{e}\n")

    @staticmethod
    def check_error_recovery() -> None:
        try:
            if GardenManager.tank <= 1:
                raise GardenError("Not enough water in tank")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("System recovered and continuing...\n")


def garden_system_test() -> None:
    print("=== Garden Management System ===\n")
    try:
        manager = GardenManager()

        tomato = Plant("tomato", 3, 8)
        lettuce = Plant("lettuce", 13, 10)
        bad_plant = Plant("", 8, 4)

        print("Adding plants to garden...")
        manager.add_plants(tomato)
        manager.add_plants(lettuce)
        manager.add_plants(bad_plant)

        print("Watering plants...")
        manager.water_plants()

        print("Checking plant health...")
        manager.check_plants_health()

        print("Testing error recovery...")
        manager.check_error_recovery()
    except Exception as e:
        print(f"Error: {e}")

    print("Garden management system test complete!")


if __name__ == "__main__":
    garden_system_test()
