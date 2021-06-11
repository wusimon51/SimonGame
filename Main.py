import tkinter as tk
from tkinter import ttk

def press_green():
    print('green')

def press_red():
    print('red')

def press_yellow():
    print('yellow')

def press_blue():
    print('blue')

def start():
    print('start')

root = tk.Tk()
root.title('Simon Game')

mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=('N, W, E, S'))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

score = tk.Label(mainframe, text='Score: ')
score.grid(column=0, row=1, sticky=('W'))

start_button = tk.Button(mainframe, text='Start', command=start)
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