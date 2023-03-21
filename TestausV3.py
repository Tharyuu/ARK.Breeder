# otetaan random int koska ei jaksa hakata aina random numeroita
from random import randint

creature1 = {}
creature2 = {}

while True:
    gender = input("Creature gender: ")
    # healt = input("Creature healt: ")
    # stamina = input("Creature stamina: ")
    # weight = input("Creature weight: ")
    # melee = input("Creature melee: ")
    healt = randint(1, 500)
    stamina = randint(1, 500)
    weight = randint(1, 500)
    melee = randint(1, 500)
    print()

    if creature1 == {}:
        creature1["healt"] = healt
        creature1["stamina"] = stamina
        creature1["weight"] = weight
        creature1["melee"] = melee

    else:
        creature2["healt"] = healt
        creature2["stamina"] = stamina
        creature2["weight"] = weight
        creature2["melee"] = melee
        break

print("Creature 1:")
print(f"Healt:\t {creature1['healt']}")
print(f"Stamina: {creature1['stamina']}")
print(f"Weight:\t {creature1['weight']}")
print(f"Melee:\t {creature1['melee']}\n")

print("Creature 2:")
print(f"Healt:\t {creature2['healt']}")
print(f"Stamina: {creature2['stamina']}")
print(f"Weight:\t {creature2['weight']}")
print(f"Melee:\t {creature2['melee']}\n")

word = "Healt"
for min, max in zip(creature1.items(), creature2.items()):
    if max < min:
        print(f"{word} {min[1]} creature1")
    elif max > min:
        print(f"{word} {max[1]} creature2")
    else:
        print(f"{word} {max[1]} same")

    if word == "Healt":
        word = word.replace("Healt", "Stamina")
    elif word == "Stamina":
        word = word.replace("Stamina", "Weight")
    else:
        word = word.replace("Weight", "Melee")
