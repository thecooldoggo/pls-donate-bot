import random
import time
import pyautogui

# PUT MESSAGES HERE!
MESSAGES = [
    "MESSAGE 1",
    "MESSAGE 2",
    "MESSAGE 3",
    "MESSAGE 4",
    "MISSEPELLED MESSAGE 1",
    "MISPELLED MESSAGE 2",
    "MISPELLED MESSAGE 3",
    "MISPELLED MESSAGE 4",
]

print("Make sure you have the chat open and you are in a game!")
print("Do not put 'robux' or anything like that or else you might get banned!")
print("Made by @thedog-bot on github.")
time.sleep(10)

while True:
    # type message in chat
    message = random.choice(MESSAGES)
    pyautogui.typewrite("/")
    time.sleep(1)
    pyautogui.typewrite(message)
    pyautogui.press("enter")
    sleep_time = random.randint(20, 110)
    time.sleep(sleep_time)
