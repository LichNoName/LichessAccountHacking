import random

from colorama import Fore, Style

all_col = [Style.BRIGHT + Fore.RED,
           Style.BRIGHT + Fore.CYAN,
           Style.BRIGHT + Fore.LIGHTCYAN_EX,
           Style.BRIGHT + Fore.LIGHTBLUE_EX,
           Style.BRIGHT + Fore.LIGHTCYAN_EX,
           Style.BRIGHT + Fore.LIGHTMAGENTA_EX,
           Style.BRIGHT + Fore.LIGHTYELLOW_EX,
           Style.BRIGHT + Fore.LIGHTGREEN_EX,

           ]

ran = random.choice(all_col)

red = all_col[0]
cyan = all_col[1]
cyanlight = all_col[2]
blue = all_col[3]
cyanlight2 = all_col[4]
magenta = all_col[5]
yellow = all_col[6]
green = all_col[7]
