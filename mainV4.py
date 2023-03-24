from colorama import Fore
creature1=[]
creature2=[]
creature3=[]
creature4=[]

while True:
    print("")
    stats=input(Fore.RESET+"All or important stats:(A/I), (Q) for quit:")
    stats=stats.lower()
    
    if stats=="q":
        print("See you later, mate!")
        break
    elif stats =="a" or stats=="i":
        amount=input("How many creatures?")
        try:
            amount=int(amount)
        except ValueError:
            print("")
            print(Fore.RED+"Wrong input, try again!")
            continue

        if amount<=0 or amount>4:
            print("")
            print(Fore.RED+"Wrong input, try again!")
        else:
            while amount>0:
                print("")
                healt=input("Healt:")
                stamina=input("Stamina:")
                weight=input("Weight:")
                melee=input("Melee:")
                
                if stats=="a":
                    oxygen=input("Oxygen:")
                    food=input("Food:")
                    speed=input("Movement speed:")
                    torpitidy=input("Torpitidy:")
                
                if creature1==[]:
                    creature1.append(f"Healt: {healt}")
                    creature1.append(f"Stamina:{stamina}")
                    creature1.append(f"Weight: {weight}")
                    creature1.append(f"Melee: {melee}")
                if stats=="a":
                    creature1.append(f"Oxygen:{oxygen}:")
                    creature1.append(f"Food:{food}")
                    creature1.append(f"Movement speed:{speed}")
                    creature1.append(f"Torpitidy:{torpitidy}")

                elif creature2==[]:
                    creature2.append(f"Healt: {healt}")
                    creature2.append(f"Stamina: {stamina}")
                    creature2.append(f"Weight: {weight}")
                    creature2.append(f"Melee: {melee}")
                if stats=="a":
                    creature2.append(f"Oxygen:{oxygen}:")
                    creature2.append(f"Food:{food}")
                    creature1.append(f"Movement speed:{speed}")
                    creature1.append(f"Torpitidy:{torpitidy}")

                elif creature3==[]:
                    creature3.append(f"Healt: {healt}")
                    creature3.append(f"Stamina: {stamina}")
                    creature3.append(f"Weight: {weight}")
                    creature3.append(f"Melee: {melee}")
                if stats=="a":
                    creature3.append(f"Oxygen:{oxygen}:")
                    creature3.append(f"Food:{food}")
                    creature1.append(f"Movement speed:{speed}")
                    creature1.append(f"Torpitidy:{torpitidy}")

                elif creature4==[]:
                    creature4.append(f"Healt: {healt}")
                    creature4.append(f"Stamina: {stamina}")
                    creature4.append(f"Weight: {weight}")
                    creature4.append(f"Melee: {melee}")
                if stats=="a":
                    creature4.append(f"Oxygen:{oxygen}:")
                    creature4.append(f"Food:{food}")
                    creature1.append(f"Movement speed:{speed}")
                    creature1.append(f"Torpitidy:{torpitidy}")
                amount-=1
    else:
        print("")
        print(Fore.RED+"Wrong input, try again!")
