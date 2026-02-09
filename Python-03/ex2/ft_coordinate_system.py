import math


def calculate_coordinates(position1: tuple, position2: tuple) -> float:
    x1, y1, z1 = position1
    x2, y2, z2 = position2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return distance


def count_coordinates(position1: tuple, coordinate: str) -> None:
    try:
        position2 = tuple(int(num) for num in coordinate.split(","))

        distance = calculate_coordinates(position1, position2)
        print(f"Parsing coordinates: \"{coordinate}\"")
        print(f"Parsed position: {position2}")
        print(f"Distance between {position1} and "
              f"{position2}: {distance:.1f}\n")

    except ValueError as e:
        print(f"Parsing invalid coordinates: \"{coordinate}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: (\"{e}\",)\n")
    except Exception as e:
        print(f"Error: {e}")


def coordinate_system() -> None:
    try:
        position1 = (0, 0, 0)
        position2 = (10, 20, 5)

        print(f"Position created: {position2}")
        distance = calculate_coordinates(position1, position2)
        print(f"Distance between {position1} and "
              f"{position2}: {distance:.2f}\n")

        coordinate = "3,4,0"
        count_coordinates(position1, coordinate)

        coordinate = "abc,def,ghi"
        count_coordinates(position1, coordinate)

        position2 = (3, 4, 0)
        x, y, z = position2
    except Exception as e:
        print(f"Error: {e}\n")

    print("Unpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    coordinate_system()
