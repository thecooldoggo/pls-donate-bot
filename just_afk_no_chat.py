import random
import time
import pyautogui
from termcolor import colored

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
    pyautogui.press("space")
    sleep_time = random.randint(10, 40)
    time.sleep(sleep_time)
