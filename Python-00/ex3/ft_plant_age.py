def ft_plant_age():
    age_in_day = int(input("Enter plant age in days: "))
    if age_in_day > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
