def garden_operations(operation: str) -> None:
    if operation == "ValueError":
        int("abc")

    elif operation == "ZeroDivisionError":
        100 / 0

    elif operation == "FileNotFoundError":
        file = open("missing.txt", "r")
        file.close()

    elif operation == "KeyError":
        garden_plants = {"rose": 5, "sunflower": 4}
        garden_plants["missing_plant"]

    elif operation == "All":
        int("abc")
        100 / 0
        file = open("missing.txt", "r")
        file.close()
        garden_plants = {"rose": 5, "sunflower": 4}
        garden_plants["missing_plant"]

    return None


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    try:
        try:
            garden_operations("ValueError")
        except ValueError as e:
            print(f"Caught ValueError: {e}\n")

        print("Testing ZeroDivisionError...")
        try:
            garden_operations("ZeroDivisionError")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}\n")

        print("Testing FileNotFoundError...")
        try:
            garden_operations("FileNotFoundError")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}\n")

        print("Testing KeyError...")
        try:
            garden_operations("KeyError")
        except KeyError as e:
            print(f"Caught KeyError: {e}\n")

        print("Testing multiple errors together...")
        try:
            garden_operations("All")
        except (ValueError, ZeroDivisionError, FileExistsError, KeyError):
            print("Caught an error, but program continues!\n")
    except Exception as e:
        print(f"Error: {e}")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
