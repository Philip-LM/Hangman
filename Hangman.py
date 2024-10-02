#backend bits of code that do the actual bits
def hangman_check(character,private,public):
    """Checks if a character is in the private list and then repalces the one in the public if so"""
    for i in range(len(private)):
        if character == private[i]:
            public[i] = private[i]
    return character,private,public

def hangman(input_word):
    run = True
    guesslist = []
    private = [x.lower() for x in input_word]
    public = ['_' for x in private]
    while run:
        guess = input('Input your character guess!\n').lower()
        rechar,private,public = hangman_check(guess,private,public)
        guesslist.append(rechar)
        if public == private:
            print('You win')
            run = False
        elif len(guesslist) == 10:
            print('You lose HAHAHAHHA loser')
            run = False



#gui bit to make it pretty
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
    
def get_priv():
    """takes the private word from the entry box"""
    global priv_word
    global priv
    priv = priv_word.get()


image_num = 1
#implimenting the guess box to get data from
text_var = tk.StringVar()
list_var = "You've guessed the letters:\n"

image_start = PhotoImage(file='images\hangman1.png')

#write word button (private)
priv_word = tk.StringVar()
priv_word_entry = ttk.Entry(window, textvariable=priv_word)
priv_word_entry_but = ttk.Entry(window, text='Submit guessing word', command=get_priv)

guess_box = ttk.Entry(window, textvariable=text_var)
guess_but = ttk.Button(window, text='submit guess', command=get_guess)
guess_list = ttk.Label(window, text = list_var)

display = ttk.Label(window, image=image_start)
# display_button = ttk.Button(window, text='change display', command=upd_disp)

display.pack()
# display_button.pack()
guess_box.pack()
guess_but.pack()
guess_list.pack()


#think it starts the window idk
window.mainloop()