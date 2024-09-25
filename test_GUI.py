import tkinter as tk
from tkinter import *
from tkinter import ttk
"""Importing random bits of tkinter, by random I mean all of it"""

#Building the actual window frame to use for the GUI
window = Tk()
window.title('Hangman')
frm = ttk.Frame(window, padding=10, width=300, height=100)

def get_guess():
    """Gets me the text from the text box as an onevent"""
    guess = text_var.get()
    print(guess)
    global new_text
    testbox.config(text = guess)



#implimenting the guess box to get data from
text_var = tk.StringVar()


guess_box = ttk.Entry(window, textvariable=text_var)
guess_but = ttk.Button(window, text='submit guess', command=get_guess,)
guess_box.pack()
guess_but.pack()


testbox = ttk.Label(window, text='no input')
testbox.pack()

#think it starts the window idk
window.mainloop()