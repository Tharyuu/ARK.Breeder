# otetaan random int koska ei jaksa hakata aina random numeroita
from random import randint

print("Creature 1:")
creature1 = {
    "gender": input("gender: "),
    "health": int(input("health: ")),
    "stamina": int(input("stamina: ")),
    "weight": int(input("weight: ")),
    "melee": int(input("melee: ")),
}
print("Creature 2:")
creature2 = {
    "gender": input("gender: "),
    "health": int(input("health: ")),
    "stamina": int(input("stamina: ")),
    "weight": int(input("weight: ")),
    "melee": int(input("melee: ")),
}

print("Creature 1:")
print(f"Healt:\t {creature1['health']}")
print(f"Stamina: {creature1['stamina']}")
print(f"Weight:\t {creature1['weight']}")
print(f"Melee:\t {creature1['melee']}\n")

print("Creature 2:")
print(f"Healt:\t {creature2['health']}")
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
