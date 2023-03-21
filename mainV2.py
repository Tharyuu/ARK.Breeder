creature1=[]
creature2=[]

while True:
    gender=input("Creature gender:")
    healt=input("Creature healt:")
    stamina=input("Creature stamina:")
    weight=input("Creature weight:")
    melee=input("Creature melee:")
    print("")
    
    if creature1==[]:
        creature1.append(healt)
        creature1.append(stamina)
        creature1.append(weight)
        creature1.append(melee)

    else:
        creature2.append(healt)
        creature2.append(stamina)
        creature2.append(weight)
        creature2.append(melee)
        break

kierros=0

for stat in creature1:
    if kierros==0:
        print(f"Healt:{stat}")
    elif kierros==1:
        print(f"Stamina:{stat}")
    elif kierros==2:
        print(f"Weight:{stat}")
    elif kierros==3:
        print(f"Melee:{stat}\n")
    kierros+=1
    
kierros=0
for stat in creature2:
    if kierros==0:
        print(f"Healt:  {stat}")
    elif kierros==1:
        print(f"Stamina:{stat}")
    elif kierros==2:
        print(f"Weight: {stat}")
    elif kierros==3:
        print(f"Melee:  {stat}\n")
    kierros+=1

word="Healt"
for min,max in zip(creature1,creature2):
    if max<min:
        print(f"{word} {min} creature1")
    elif max>min:
        print(f"{word} {max} creature2")
    else:
        print(f"{word} {max} same")
    
    if word=="Healt":
        word=word.replace("Healt", "Stamina")
    elif word=="Stamina":
        word=word.replace("Stamina","Weight")
    else:
        word=word.replace("Weight","Melee")