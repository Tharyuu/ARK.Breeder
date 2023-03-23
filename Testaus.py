creature1=[]

while True:
    stats=input("All or important stats:(A/I), (Q) for quit:")
    quit=stats.lower()
    all=stats.lower()
    important=stats.lower()

    if stats!="a" or stats!="i" or stats!="q":
        print("Wrong input, try again!")
    elif quit=="q":
        break
    
    amount=int(input("How many creatures?"))
    healt=input("Healt:")
    
    if all=="a":
        oxygen=input("Oxygen:")
    
    if creature1==[]:
        creature1.append(f"Healt: {healt}")
        if all=="a":
            creature1.append(f"Oxygen:{oxygen}:")
    
    print(creature1)