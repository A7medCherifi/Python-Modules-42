import sys


def current_inventory(inventory: dict, total_items: int) -> None:
    print("\n=== Current Inventory ===")
    try:
        inventories = set()
        for key, value in inventory.items():
            quantity = value
            percentage = (quantity / total_items) * 100
            inventories.add((key, quantity, percentage))

        for key, quantity, percentage in inventories:
            print(f"{key}: {quantity} units ({percentage:.1f}%)")
    except Exception as e:
        print(f"Error: {e}")


def inventory_statistics(inventory: dict) -> None:
    print("\n=== Inventory Statistics ===")
    try:
        max_val = 0
        max_item = ""
        min_item = ""

        for key, value in inventory.items():
            if value > max_val:
                max_val = value
                max_item = key

        min_val = max_val
        for key, value in inventory.items():
            if len(inventory) == 1:
                min_val = value
                min_item = key
                break
            if value < min_val:
                min_val = value
                min_item = key

        print(f"Most abundant: {max_item} ({max_val} units)")
        print(f"Least abundant: {min_item} ({min_val} units)")
    except Exception as e:
        print(f"Error: {e}")


def item_categories(inventory: dict) -> None:
    print("\n=== Item Categories ===")
    try:
        if len(inventory["abundant"]) > 0:
            print(f"Abundant: {inventory["abundant"]}")
        if len(inventory["moderate"]) > 0:
            print(f"Moderate: {inventory["moderate"]}")
        if len(inventory["scarce"]) > 0:
            print(f"Scarce: {inventory["scarce"]}")

    except Exception as e:
        print(f"Error: {e}")


def management_suggestions(inventory: dict) -> None:
    print("\n=== Management Suggestions ===")
    try:
        restock = []
        for key, value in inventory.items():
            if value <= 3:
                restock += [key]

        print(f"Restock needed: {restock}")
    except Exception as e:
        print(f"Error: {e}")


def dictionary_properties(inventory: dict) -> None:
    print("\n=== Dictionary Properties Demo ===")
    try:
        lookup_item = False
        dic_keys = []
        dic_values = []
        for key, value in inventory.items():
            if key == 'sword':
                lookup_item = True
            dic_keys += [key]
            dic_values += [value]

        print(f"Dictionary keys: {dic_keys}")
        print(f"Dictionary values: {dic_values}")
        print(f"Sample lookup - 'sword' in inventory: {lookup_item}")
    except Exception as e:
        print(f"Error: {e}")


def inventory_system() -> None:
    inventory = dict()
    categories = {
        "abundant": {},
        "moderate": {},
        "scarce": {}
    }
    try:
        if len(sys.argv) == 1:
            raise Exception("YOU BASTARD add some arguments !!")
        i = 1
        while i < len(sys.argv):
            name, value = sys.argv[i].split(':')
            inventory.update({name: int(value)})
            i += 1
        for key, value in inventory.items():
            if value < 0:
                raise Exception("the quantity can't be < 0, stupid.")
            if value > 5:
                categories["abundant"][key] = value
            elif 3 < value <= 5:
                categories["moderate"][key] = value
            else:
                categories["scarce"][key] = value
    except Exception as e:
        print(f"Error: {e}")
        return

    total_items = 0
    unique_items = 0
    for value in inventory.values():
        unique_items += 1
        total_items += value

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_items}")

    try:
        current_inventory(inventory, total_items)
        inventory_statistics(inventory)
        item_categories(categories)
        management_suggestions(inventory)
        dictionary_properties(inventory)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===\n")
    inventory_system()
