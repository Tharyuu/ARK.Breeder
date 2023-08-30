"""
ARK Breeder stats comparator thingy.
Original Author: Tharyuu-desu;
github.com/Tharyuu-desu

Whacked by jukkav1. Appologies.

"""
from colorama import Fore

DEBUG = True
if DEBUG:
    from random import randint

FORES = [Fore.RED, Fore.BLUE, Fore.YELLOW, Fore.GREEN]


class Creature:
    """a generic idea of what a creature is"""

    def __init__(self, fore) -> None:
        self.fore = fore
        self.stats = ask_stats()


def get_string(text: str) -> str:
    """forced input a string"""
    while 1:
        try:
            user_input = input(text)
            if user_input.isalpha():
                str(user_input)
                return user_input
            continue

        except ValueError:
            print("Try again!")
            continue


def get_float(text: str) -> int:
    """force user to give a float"""

    # jos ei jaksa, arvo jotain 0 .. 200
    if DEBUG:
        return randint(0, 200)

    while 1:
        try:
            user_input = input(text)
            float(user_input)
            return user_input

        except ValueError:
            print("Try again!")
            continue


def get_char(text: str, char_list: list) -> str:
    """Force user to give a string containing a character listed in char_list:list"""
    while 1:
        try:
            user_input = input(text)
            str(user_input).lower()
            for _ in char_list:
                if _ in user_input.lower():
                    return _

        except ValueError:
            print("Try again!")
            continue


def ask_stats() -> dict:
    """ask for stats forcing input"""
    stats = {}
    stats["name"] = str(get_string("Give Creature:"))
    stats["level"] = float(get_float("Give Wild Level:"))
    stats["gender"] = str(get_char("Give Gender ([F]emale / [M]ale):", ["f", "m"]))
    stats["health"] = float(get_float("Give Healt:"))
    stats["stamina"] = float(get_float("Give Stamina:"))
    stats["weight"] = float(get_float("Give Weight:"))
    stats["melee"] = float(get_float("Give Melee:"))
    return stats


def main():
    """THE main loop"""
    creatures = []
    print("Welcome to ARK Breeder!")
    print("Let us begin!")
    while 1:
        try:
            how_many = int(input("how many creatures?: "))
        except ValueError:
            print("Thats not a number!")
            break

        # tämä for tekee miljoona asiaa
        for _ in range(how_many):
            fore = FORES[_ % len(FORES) - 1]
            print(fore + "", end="")
            new_creature = Creature(fore)
            creatures.append(new_creature)
        break

    for crea in creatures:
        print(f"{crea.fore}{crea.stats}")


if __name__ == "__main__":
    main()
