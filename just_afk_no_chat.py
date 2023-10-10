import random
import time
import pyautogui
from termcolor import colored

print(colored('Make sure you are in a game! You have 30 before the script starts.', 'green', 'on_green', ['bold', 'underline']))
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
print(colored('Quit this window to end the script!', 'yellow', 'on_yellow', ['bold']))
while True:
    pyautogui.press("space")
    sleep_time = random.randint(10, 40)
    time.sleep(sleep_time)