def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    if days <= 0:
        print("Harvest time!")
        return
    def recursive(day):
        if day > days:
            print("Harvest time!")
            return
        print(f"Day {day}")
        recursive(day + 1)
    recursive(1)
