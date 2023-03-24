"""from colorama import Fore                                                            # We pass **kwargs so we can use other print() function's keyword arguments, such as end and sep.

FORES = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE]

def print_with_color(s, color=Fore.WHITE,**kwargs):                                  
    print(f"{color}{s}", **kwargs)
    sana=input("Anna sana:")

for fore in FORES:
    
        print_with_color("Hello world!", color=fore,)"""

from colorama import Fore

FORES=[Fore.RED,Fore.BLUE,Fore.YELLOW,Fore.GREEN]
crature="Rex"
creature=input("Creature:")

def colored_stats(s,color=Fore.RED,**kwargs):
    print(f"{color}{s}")
    healt=input("Healt:")
    
for fore in FORES:
    print("")
    colored_stats(f"Creature:{creature}",color=fore)

print(Fore.RESET)


from colorama import Fore

FORES=[Fore.RED,Fore.BLUE,Fore.YELLOW,Fore.GREEN]
creature=input("Creature:")
amount=7


def colored_stats(s,color=Fore.RED,**kwargs):
    print(f"{color}{s}")
    healt=input("Healt:")
    
for fore in FORES:
    print("")
    colored_stats(f"Creature:{creature}",color=fore)
    amount-=1
    if amount==0:
        break

print(Fore.RESET)