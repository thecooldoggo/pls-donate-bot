import asyncio
import webbrowser
import pyautogui
import time

async def main():
    print("Welcome to the pls donate bot!")
    print("Made by @thedog-bot bot on github")
    print("Make sure you have the game open and are not tabbed out!")
    await asyncio.sleep(3)
    webbrowser.open('https://www.roblox.com/games/8737602449')
    await asyncio.sleep(30)
    while True:
        pyautogui.typewrite("/")
        time.sleep(1)
        pyautogui.typewrite("WRITE CUSTOM MESSAGE 1")
        pyautogui.press("enter")
        time.sleep(15)
        pyautogui.typewrite("/")
        time.sleep(1)
        pyautogui.typewrite("CHANGE ME 2")
        pyautogui.press("enter")
        time.sleep(15)
if __name__ == "__main__":    asyncio.get_event_loop().run_until_complete(main())
