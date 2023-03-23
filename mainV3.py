# list
creature1 = []
creature2 = []
creature3 = []
creature4 = []
creature5 = []
creature6 = []

while True:
    amount = int(input("How many creatures?"))
    stats = input("All or important stats:(A/I), (Q) for quit:")
    quit = stats.lower()
    all = stats.lower()

    if quit == "q":
        break
    healt = input("Healt:")
    stamina = input("Stamina:")
    weight = input("Weight:")
    melee = input("Melee:")

    if all == "a":
        oxygen = input("Oxygen:")
        food = input("Food:")
        speed = input("Movement speed:")
        torpitidy = input("Torpitidy:")

    elif creature1 == []:
        creature1.append(f"Healt: {healt}")
        creature1.append(f"Stamina: {stamina}")
        creature1.append(f"Weight: {weight}")
        creature1.append(f"Melee: {melee}")
        if all == "a":
            creature1.append(f"Oxygen:{oxygen}:")
            creature1.append(f"Food:{food}")
            creature1.append(f"Movement speed:{speed}")
            creature1.append(f"Torpitidy:{torpitidy}")

    elif creature2 == []:
        creature2.append(f"Healt: {healt}")
        creature2.append(f"Stamina: {stamina}")
        creature2.append(f"Weight: {weight}")
        creature2.append(f"Melee: {melee}")
        if all == "a":
            creature2.append(f"Oxygen:{oxygen}:")
            creature2.append(f"Food:{food}")
            creature1.append(f"Movement speed:{speed}")
            creature1.append(f"Torpitidy:{torpitidy}")

    elif creature3 == []:
        creature3.append(f"Healt: {healt}")
        creature3.append(f"Stamina: {stamina}")
        creature3.append(f"Weight: {weight}")
        creature3.append(f"Melee: {melee}")
        if all == "a":
            creature3.append(f"Oxygen:{oxygen}:")
            creature3.append(f"Food:{food}")
            creature1.append(f"Movement speed:{speed}")
            creature1.append(f"Torpitidy:{torpitidy}")

    elif creature4 == []:
        creature4.append(f"Healt: {healt}")
        creature4.append(f"Stamina: {stamina}")
        creature4.append(f"Weight: {weight}")
        creature4.append(f"Melee: {melee}")
        if all == "a":
            creature4.append(f"Oxygen:{oxygen}:")
            creature4.append(f"Food:{food}")
            creature1.append(f"Movement speed:{speed}")
            creature1.append(f"Torpitidy:{torpitidy}")

    elif creature5 == []:
        creature5.append(f"Healt: {healt}")
        creature5.append(f"Stamina: {stamina}")
        creature5.append(f"Weight: {weight}")
        creature5.append(f"Melee: {melee}")
        if all == "a":
            creature5.append(f"Oxygen:{oxygen}:")
            creature5.append(f"Food:{food}")
            creature1.append(f"Movement speed:{speed}")
            creature1.append(f"Torpitidy:{torpitidy}")
    else:
        creature6.append(f"Healt: {healt}")
        creature6.append(f"Stamina: {stamina}")
        creature6.append(f"Weight: {weight}")
        creature6.append(f"Melee: {melee}")
        if all == "a":
            creature6.append(f"Oxygen:{oxygen}:")
            creature6.append(f"Food:{food}")
            creature1.append(f"Movement speed:{speed}")
            creature1.append(f"Torpitidy:{torpitidy}")
amount -= 1

print(creature1)
print(creature2)
print(creature3)
print(creature4)
print(creature5)
print(creature6)
