def check_plant_health(plant: str, water_level: int, sunlights: int) -> str:
    if not plant:
        raise ValueError("Plant name can not be empty!")

    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")

    if sunlights < 2:
        raise ValueError(f"Sunlight hours {sunlights} is too low (min 2)")
    if sunlights > 12:
        raise ValueError(
            f"Sunlight hours {sunlights} is too high (max 12)")

    return f"Plant '{plant}' is healthy!\n"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 10, 10))
    except ValueError as e:
        print(f"Error: {e}\n")
    except Exception as e:
        print(f"Error: {e}\n")

    print("Testing empty plant...")
    try:
        print(check_plant_health("", 10, 10))
    except ValueError as e:
        print(f"Error: {e}\n")
    except Exception as e:
        print(f"Error: {e}\n")

    print("Testing bad water level...")
    try:
        print(check_plant_health("tomato", 15, 10))
    except ValueError as e:
        print(f"Error: {e}\n")
    except Exception as e:
        print(f"Error: {e}\n")

    print("Testing bad sunlight hours...")
    try:
        print(check_plant_health("tomato", 10, 0))
    except ValueError as e:
        print(f"Error: {e}\n")
    except Exception as e:
        print(f"Error: {e}\n")

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
