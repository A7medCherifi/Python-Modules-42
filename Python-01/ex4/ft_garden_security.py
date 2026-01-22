class SecurePlant:
    """Blueprint of the plant"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Store the plant info and Display the creation"""
        self.name = name
        self.__height = height
        self.__age = age
        print(f"Plant created: {self.name}")

    def set_height(self, high) -> None:
        """To modify the height value and prevent invalid input"""
        if high < 0:
            print(f"\nInvalid operation attempted: height {high}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = high
            print(f"Height updated: {high}cm [OK]")

    def set_age(self, age) -> None:
        """To modify the age value and prevent invalid input"""
        if age < 0:
            print(f"\nInvalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative Age rejected")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self) -> int:
        """To display the height value"""
        return self.__height

    def get_age(self) -> int:
        """To display the age value"""
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 15, 10)
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    print(f"\nCurrent plant: {rose.name} ({rose.get_height()}cm, "
          f"{rose.get_age()} days)")
