import random
import time
import pyautogui
from termcolor import colored

# PUT MESSAGES HERE!
MESSAGES = [
    "MESSAGE 1",
    "MESSAGE 2",
    "MESSAGE 3",
    "MISPELLED MESSAGE 1",
    "MISPELLED MESSAGE 2",
    "MISPELLED MESSAGE 3",
]

print(colored('Do not put "robux" or anything like that or else you might get banned!', 'white', 'on_red', ['bold', 'underline']))
print(colored('Made by @thedog-bot on github.', 'white', 'on_green', ['bold', 'underline']))
print(colored('Make sure you are in a game! You have 30 before the script starts.', 'white', 'on_yellow', ['bold', 'underline']))
time.sleep(25)
print(colored('5...', 'white', 'on_red', ['bold']))
time.sleep(1)
print(colored('4...', 'white', 'on_red', ['bold']))
time.sleep(1)
print(colored('3...', 'white', 'on_red', ['bold']))
time.sleep(1)
print(colored('2...', 'white', 'on_red', ['bold']))
time.sleep(1)
print(colored('1...', 'white', 'on_red', ['bold']))
time.sleep(1)
print(colored('Quit this window to end the script!', 'white', 'on_blue', ['bold']))

while True:
    # type message in chat
    message = random.choice(MESSAGES)
    pyautogui.typewrite("/")
    time.sleep(1)
    pyautogui.typewrite(message)
    pyautogui.press("enter")
    sleep_time = random.randint(20, 110)
    time.sleep(sleep_time)
