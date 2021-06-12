import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
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
    global player_state, player_queue 
    if player_state:
        player_queue.append('green')


def press_red():
    global player_state, player_queue
    if player_state:
        player_queue.append('red')


def press_yellow():
    global player_state, player_queue
    if player_state:
        player_queue.append('yellow')


def press_blue():
    global player_state, player_queue
    if player_state:
        player_queue.append('blue')


def game_threading():
    event = Event()
    t1 = Thread(target=start, args=(event,))
    t1.daemon = True
    t1.start()


def restart(window):
    global game_queue, player_queue, score, score_label
    window.destroy()
    game_queue = player_queue = []
    score = 0
    score_label.configure(text='Score: 0') 
    game_threading()


def lose_box():
    top = tk.Toplevel(root)
    top.title('Game Over')
    top.geometry(f'250x100+{root.winfo_x() + int(root.winfo_width() / 4)}+{root.winfo_y() + int(root.winfo_height() / 4)}')

    message = tk.Label(top, text='You lose! Retry?', height=2).pack()
    yes_button = tk.Button(top, text='Yes', command=lambda: restart(top)).pack(side=tk.LEFT, padx=40)
    no_button = tk.Button(top, text='No', command=quit).pack(side=tk.RIGHT, padx=40)


def start(e):
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
    has_lost = False
    while not has_lost:
        global player_queue, game_queue, score, score_label, player_state
        player_queue = []
        game_queue.append(choose_color())
        # display current sequence to player
        for color in game_queue:
            button = buttons[color]
            time.sleep(0.5)
            button.configure(bg='white')
            time.sleep(0.5)
            button.configure(bg=button_colors[color])
            time.sleep(0.5)
        current_index = 0
        # get player input
        player_state = True
        while current_index < len(game_queue):
            try:
                if player_queue[current_index] == game_queue[current_index]:
                    current_index += 1
                else:
                    has_lost = True
                    break
            except IndexError:
                continue
        if not has_lost:
            score += 1
            player_state = False
            score_label.configure(text='Score: '+str(score))
    lose_box()        
    player_state = False

# initial window setup
root = tk.Tk()
root.title('Simon Game')

mainframe = ttk.Frame(root, padding='4 4 4 4')
mainframe.grid(column=0, row=0, sticky=('N, W, E, S'))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# score label and start button at the top
score_label = tk.Label(mainframe, text='Score: ' + str(score), height=2)
score_label.grid(column=0, row=1, sticky=('W'))

start_button = tk.Button(mainframe, text='Start', width=4, command=game_threading)
start_button.grid(column=1, row=1, sticky='E')

# main game buttons
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
