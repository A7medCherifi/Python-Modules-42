class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


def check_plants_health() -> None:
    plants = {"tomato": 20, "botato": 30, "carrot": 50}
    for plant, value in plants.items():
        if value < 30:
            raise PlantError(f"The {plant} plant is wilting!")


def check_plants_water(tank: int) -> None:
    if tank < 10:
        raise WaterError("Not enough water in the tank!")


def test_garden_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        try:
            check_plants_health()
            print("Plants are healthy.\n")
        except PlantError as e:
            print(f"Caught PlantError: {e}\n")

        print("Testing WaterError...")
        try:
            check_plants_water(5)
            print("Tank still has enough water.\n")
        except WaterError as e:
            print(f"Caught WaterError: {e}\n")

        print("Testing catching all garden errors...")
        try:
            check_plants_health()
        except GardenError as e:
            print(f"Caught a garden error: {e}")

        try:
            check_plants_water(5)
        except GardenError as e:
            print(f"Caught a garden error: {e}")
    except Exception as e:
        print(f"Error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_garden_errors()
