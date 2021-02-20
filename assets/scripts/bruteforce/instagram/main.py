import instagram
import os
from lib.const import modes
from termcolor import colored

print("""
0 —› 32 бота
1 —› 16 ботов
2 —› 8 ботов
3 —› 4 бота
""")

mode = int(input(
    colored("mode> ", "magenta")
))

username = input(
    colored("nickname> ", "magenta")
)

engine = instagram.Engine(
    username,
    modes[mode],
    os.path.join("..", "passlist_instagram.txt"),
    True
)
engine.start()
