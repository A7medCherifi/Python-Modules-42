def water_plants(plant_list: list) -> None:
    try:
        for plant in plant_list:
            if plant is None:
                raise Exception(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
        print("Watering completed successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)\n")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    valid_list = ["tomato", "lettuce", "carrots"]
    invalid_list = ["tomato", None]

    try:
        print("Testing normal watering...")
        print("Opening watering system")
        water_plants(valid_list)

        print("Testing with error...")
        print("Opening watering system")
        water_plants(invalid_list)
    except Exception as e:
        print(f"{e}")

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
