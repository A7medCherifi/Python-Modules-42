def check_temperature(temp_str: str) -> None:
    print(f"Testing temperature: {temp_str}")

    try:
        temp_int = int(temp_str)
        if 0 <= temp_int <= 40:
            print(f"Temperature {temp_int}°C is perfect for plants!\n")
        elif temp_int > 40:
            print(f"Error: {temp_int}°C is too hot for plants (max 40°C)\n")
        else:
            print(f"Error: {temp_int}°C is too cold for plants (min 0°C)\n")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")


def test_temperature_input() -> None:
    try:
        check_temperature("25")
        check_temperature("abc")
        check_temperature("100")
        check_temperature("-50")
        print("All tests completed - program didn't crash!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()
