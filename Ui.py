import random
import time
import pyautogui
import tkinter as tk
from threading import Thread
from tkinter import PhotoImage

running = False

def main_loop():
    global running
    running = True
    while running:
        # type message in chat
        message = random.choice(MESSAGES)
        pyautogui.typewrite("/")
        time.sleep(1)
        pyautogui.typewrite(message)
        pyautogui.press("enter")
        sleep_time = random.randint(20, 110)
        time.sleep(sleep_time)

def stop():
    global running
    running = False

window = tk.Tk()
window.title("Pls Donate Bot")
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack(fill="both", expand=True)
bg_image = PhotoImage(file="bg1.png")
canvas.create_image(0, 0, image=bg_image, anchor="nw")

label = tk.Label(text="Enter your messages to send above: (one per line)")
label.pack()

def get_messages():
    text = message_entry.get("1.0", "end-1c")
    return text.split('\n')

def start():
    global MESSAGES
    MESSAGES = get_messages()
    Thread(target=main_loop).start()

canvas_width = 800
canvas_height = 600
message_entry = tk.Text(window, font=("Helvetica", 16), bg="#2c2d2e", fg="#cccbc8")
canvas.create_window(canvas_width//2, canvas_height//2, window=message_entry)

def start_with_delay():
    time.sleep(5)
    start()
start_button = tk.Button(window, text="Start Script", command=start_with_delay)
start_button.pack()

stop_button = tk.Button(window, text="Stop Script", command=stop)
stop_button.pack()

window.mainloop()