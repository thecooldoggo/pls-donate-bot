import random
import time
import pyautogui
from termcolor import colored

# PUT MESSAGES HERE!
MESSAGES = [
    "hello there!",
    "/e 1",
    "donate for the dogs?",
    "have an amazing day!",
    "helo there.",
    "donote fo the dogs?",
    "Hav an amazin day!",
]

print(colored('Do not put "robux" or anything like that or else you might get banned!', 'red', 'on_red', ['bold', 'underline']))
print(colored('Made by @thedog-bot on github.', 'green', 'on_green', ['bold', 'underline']))
print(colored('Make sure you are in a game! You have 30 before the script starts.', 'yellow', 'on_yellow', ['bold', 'underline']))
time.sleep(25)
print(colored('5...', 'red', 'on_red', ['bold']))
time.sleep(1)
print(colored('4...', 'red', 'on_red', ['bold']))
time.sleep(1)
print(colored('3...', 'red', 'on_red', ['bold']))
time.sleep(1)
print(colored('2...', 'red', 'on_red', ['bold']))
time.sleep(1)
print(colored('1...', 'red', 'on_red', ['bold']))
time.sleep(1)
print(colored('Quit this window to end the script!', 'blue', 'on_blue', ['bold']))

while True:
    # type message in chat
    message = random.choice(MESSAGES)
    pyautogui.typewrite("/")
    time.sleep(1)
    pyautogui.typewrite(message)
    pyautogui.press("enter")
    sleep_time = random.randint(20, 110)
    time.sleep(sleep_time)
