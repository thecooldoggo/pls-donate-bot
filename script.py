import asyncio
from dotenv import load_dotenv
import webbrowser
import pyautogui
import time
load_dotenv()

async def main():
    print("Welcome, to the pls donate bot!")
    await asyncio.sleep(3)
    webbrowser.open('https://www.roblox.com/games/8737602449')
    await asyncio.sleep(30)
    while True:
        pyautogui.typewrite("/")
        time.sleep(1)
        pyautogui.typewrite("PUT MESSAGE 1 HERE")
        pyautogui.press("enter")
        time.sleep(15)
        pyautogui.typewrite("/")
        time.sleep(1)
        pyautogui.typewrite("PUT MESSAGE 2 HERE")
        time.sleep(15)
if __name__ == "__main__":    asyncio.get_event_loop().run_until_complete(main())
