def current_inventory(inventory: dict, total_items: int):
    print("\n=== Current Inventory ===")
    try:
        inventories = set()
        for key, value in inventory.items():
            quantity = value.get('quantity')
            percentage = (quantity / total_items) * 100
            inventories.add((key, quantity, percentage))

        for key, quantity, percentage in inventories:
            print(f"{key}: {quantity} units ({percentage:.1f}%)")
    except Exception as e:
        print(f"Error: {e}")


def inventory_statistics(inventory: dict):
    print("\n=== Inventory Statistics ===")
    try:
        max_val = 0
        max_item = ""
        min_item = ""

        for key, value in inventory.items():
            if value.get('quantity') > max_val:
                max_val = value.get('quantity')
                max_item = key

        min_val = max_val
        for key, value in inventory.items():
            if value.get('quantity') < min_val:
                min_val = value.get('quantity')
                min_item = key

        print(f"Most abundant: {max_item} ({max_val})")
        print(f"Least abundant: {min_item} ({min_val})")
        return min_val
    except Exception as e:
        print(f"Error: {e}")


def item_categories(inventory: dict):
    print("\n=== Item Categories ===")
    try:
        moderate = dict()
        scarce = dict()
        for key, value in inventory.items():
            if value.get('value') == "most":
                scarce.update({key: value.get('quantity')})
            if value.get('value') == "least":
                moderate.update({key: value.get('quantity')})

        print(f"Moderate: {moderate}")
        print(f"Scarce: {scarce}")
    except Exception as e:
        print(f"Error: {e}")


def management_suggestions(inventory: dict, min_val: int):
    print("\n=== Management Suggestions ===")
    try:
        restock = []
        for key, value in inventory.items():
            if value.get('quantity') == min_val:
                restock += [key]

        print(f"Restock needed: {restock}")
    except Exception as e:
        print(f"Error: {e}")


def dictionary_properties(inventory: dict):
    print("\n=== Dictionary Properties Demo ===")
    try:
        lookup_item = False
        dic_keys = []
        dic_values = []
        for key, value in inventory.items():
            if key == 'sword':
                lookup_item = True
            dic_keys += [key]
            dic_values += [value.get('quantity')]

        print(f"Dictionary keys: {dic_keys}")
        print(f"Dictionary values: {dic_values}")
        print(f"Sample lookup - 'sword' in inventory: {lookup_item}")
    except Exception as e:
        print(f"Error: {e}")


def inventory_system():
    inventory = {
        "sword": {
            "type": "weapon",
            "value": "most",
            "quantity": 1
        },
        "potion": {
            "type": "consumable",
            "value": "least",
            "quantity": 5
        },
        "shield": {
            "type": "armor",
            "value": "most",
            "quantity": 2
        },
        "armor": {
            "type": "armor",
            "value": "most",
            "quantity": 3
        },
        "helmet": {
            "type": "armor",
            "value": "most",
            "quantity": 1
        }
    }

    total_items = 0
    unique_items = 0
    for value in inventory.values():
        unique_items += 1
        total_items += value.get('quantity')

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_items}")

    current_inventory(inventory, total_items)
    min_val = inventory_statistics(inventory)
    item_categories(inventory)
    management_suggestions(inventory, min_val)
    dictionary_properties(inventory)

if __name__ == "__main__":
    print("=== Inventory System Analysis ===\n")
    inventory_system()
