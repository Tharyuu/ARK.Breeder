from colorama import Fore

FORES = [Fore.RED, Fore.BLUE, Fore.YELLOW, Fore.GREEN]


def colored_stats(color=Fore.RED, **kwargs):
    creature = input(f"{color}Creature:")
    healt = input("Healt:")
    if stats == "a":
        oxygen = input("Oxygen:")


while True:
    print("")
    stats = input(Fore.RESET + "All or important stats:(A/I), (Q) for quit:")
    stats = stats.lower()

    if stats == "q":
        print("See you later, mate!")
        break
    elif stats == "a" or stats == "i":
        amount = input("How many creatures?(1-4):")
        try:
            amount = int(amount)
        except ValueError:
            print("")
            print(Fore.MAGENTA + "Wrong input, try again!")
            continue

        if amount <= 0 or amount > 4:
            print("")
            print(Fore.MAGENTA + "Wrong input, try again!")
        else:
            while amount > 0:
                for fore in FORES:
                    print("")
                    colored_stats(color=fore)
                    amount -= 1
                    if amount == 0:
                        break
    else:
        print("")
        print(Fore.MAGENTA + "Wrong input, try again!")
