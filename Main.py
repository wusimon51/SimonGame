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

root = tk.Tk()
root.title('Simon Game')

mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=('N, W, E, S'))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

score = tk.Label(mainframe, text='Score: ')
score.grid(column=0, row=1, sticky=('W'))

green_button = tk.Button(mainframe, text='', command=press_green, bg='green')
green_button.grid(column=0, row=2, sticky='W')

red_button = tk.Button(mainframe, text='', command=press_red, bg='red')
red_button.grid(column=1, row=2, sticky='E')

yellow_button = tk.Button(mainframe, text='', command=press_yellow, bg='yellow')
yellow_button.grid(column=0, row=3, sticky='W')

blue_button = tk.Button(mainframe, text='', command=press_blue, bg='blue')
blue_button.grid(column=1, row=3, sticky='E')

root.mainloop()
