from colorama import Fore

FORES=[Fore.RED,Fore.BLUE,Fore.YELLOW,Fore.GREEN]

while True:
    print("")
    stats=input(Fore.RESET+"All or important stats:(A/I), (Q) for quit:")
    stats=stats.lower()
    
    if stats=="q":
        print("See you later, mate!")
        break
    elif stats =="a" or stats=="i":
        amount=input("How many creatures?(1-4):")
        try:
            amount=int(amount)
        except ValueError:
            print("")
            print(Fore.MAGENTA+"Wrong input, try again!")
            continue

        if amount<=0 or amount>4:
            print("")
            print(Fore.MAGENTA+"Wrong input, try again!")
        else:
            while amount>0:
                creature=input("Creature:")
                def colored_stats(s,color=Fore.RED,**kwargs):
                    print(f"{color}{s}")
                    healt=input("Healt:")
                    if stats=="a":
                        oxygen=input("Oxygen:")
    
                for fore in FORES:
                    print("")
                    colored_stats(f"Creature:{creature}",color=fore)
                    amount-=1
                    if amount==0:
                        break
    else:
        print("")
        print(Fore.MAGENTA+"Wrong input, try again!")
