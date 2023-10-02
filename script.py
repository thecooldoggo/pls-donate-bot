import pyautogui
import time
import random

print("Welcome to the pls donate bot!")
print("Made by @thedog-bot bot on github")
print("Make sure you have the game open and are not tabbed out!")
print("Do not put 'robux' or anything like that or else you might get banned!")
time.sleep(10)

message_count = 0
while True:
    pyautogui.typewrite("/")
    time.sleep(1)
    pyautogui.typewrite("CUSTOM MESSAGE 1")
    pyautogui.press("enter")
    message_count += 1
    if message_count % random.randint(3, 7) == 0:
        pyautogui.typewrite("/")
        time.sleep(1)
        pyautogui.typewrite("MISSPELLED MESSAGE 1")
        pyautogui.press("enter")
    sleep_time = random.randint(20, 100)
    time.sleep(sleep_time)
    pyautogui.typewrite("/")
    time.sleep(1)
    pyautogui.typewrite("MESSAGE 2")
    pyautogui.press("enter")
    if message_count % random.randint(3, 7) == 0:
        pyautogui.typewrite("/")
        time.sleep(1)
        pyautogui.typewrite("MISSPELLED MESSAGE 2")
        pyautogui.press("enter")
    message_count += 1
    sleep_time = random.randint(20, 100)
    time.sleep(sleep_time)
