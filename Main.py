import tkinter as tk
from tkinter import ttk
import random
import time
from threading import *

score = 0
player_state = False
game_queue = []
player_queue = []


def choose_color():
    colors = ['green', 'red', 'yellow', 'blue']
    num = random.randint(0, 3)
    return colors[num]


def press_green():
    print('green')


def press_red():
    print('red')


def press_yellow():
    print('yellow')


def press_blue():
    print('blue')


def game_threading():
    t1 = Thread(target=start)
    t1.start();


def start():
    start_button['state'] = 'disabled'
    buttons = {
        'green': green_button,
        'red': red_button,
        'yellow': yellow_button,
        'blue': blue_button
    }
    button_colors = {
        'green': '#30d94c',
        'red': '#e92539',
        'yellow': '#f8f120',
        'blue': '#1470d2'
    }
    while True:
        game_queue.append(choose_color())
        print(game_queue)
        for color in game_queue:
            button = buttons[color]
            button.configure(bg='white')
            time.sleep(0.5)
            button.configure(bg=button_colors[color])
            time.sleep(0.5)
        


root = tk.Tk()
root.title('Simon Game')

mainframe = ttk.Frame(root, padding='4 4 4 4')
mainframe.grid(column=0, row=0, sticky=('N, W, E, S'))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

score = tk.Label(mainframe, text='Score: ' + str(score), height=2)
score.grid(column=0, row=1, sticky=('W'))

start_button = tk.Button(mainframe, text='Start', width=4, command=game_threading)
start_button.grid(column=1, row=1, sticky='E')

pixel = tk.PhotoImage(width=1, height=1)

green_button = tk.Button(mainframe, text='', image=pixel, width=150, height=150, command=press_green, bg='#30d94c')
green_button.grid(column=0, row=2, sticky='W')

red_button = tk.Button(mainframe, text='', image=pixel, width=150, height=150, command=press_red, bg='#e92539')
red_button.grid(column=1, row=2, sticky='E')

yellow_button = tk.Button(mainframe, text='', image=pixel, width=150, height=150, command=press_yellow, bg='#f8f120')
yellow_button.grid(column=0, row=3, sticky='W')

blue_button = tk.Button(mainframe, text='', image=pixel, width=150, height=150, command=press_blue, bg='#1470d2')
blue_button.grid(column=1, row=3, sticky='E')

root.mainloop()
