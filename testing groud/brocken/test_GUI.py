import tkinter as tk
from tkinter import *
from tkinter import ttk
"""Importing random bits of tkinter, by random I mean all of it"""

#Building the actual window frame to use for the GUI
window = Tk()
window.geometry("500x400")
window.title('Hangman')
frm = ttk.Frame(window, padding=10, width=3000, height=100)

def get_guess():
    """Gets me the text from the text box as an onevent"""
    global list_var
    guess = text_var.get()
    if guess not in list_var[26:]:
        list_var += guess
    guess_list.config(text = list_var)

def upd_disp():
    """changes the display image"""
    global image_num
    global image_state
    image_num += 1
    image_path = 'images\hangman' + str(image_num) + '.png'
    image_state = PhotoImage(file=str(image_path))
    display.config(image=image_state)
    

image_num = 1
#implimenting the guess box to get data from
text_var = tk.StringVar()
list_var = "You've guessed the letters:\n"

image_start = PhotoImage(file='images\hangman1.png')

guess_box = ttk.Entry(window, textvariable=text_var)
guess_but = ttk.Button(window, text='submit guess', command=get_guess)
guess_list = ttk.Label(window, text = list_var)

display = ttk.Label(window, image=image_start)
display_button = ttk.Button(window, text='change display', command=upd_disp)

display.pack()
display_button.pack()
guess_box.pack()
guess_but.pack()
guess_list.pack()


#think it starts the window idk
window.mainloop()