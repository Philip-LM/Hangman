playing = False

def hangman(word):
    """Cleans my inputs and updates my public disp"""
    global public_disp
    global private_list
    global playing

    #literally just is a boolean for an odd state
    playing = TRUE

    private_list = [x.lower() for x in word]
    public_disp = ['_' for x in word]
    public_word_label.config(text=public_disp)

def hangman_check(letter):
    """Will validate if a letter is in my private string and update accordingly"""
    global public_disp
    global private_list
    global list_var
    global win_screen

    temp = [x for x in public_disp]

    for i in range(len(private_list)):
        if letter == private_list[i]:
            public_disp[i] = private_list[i]
    
    if temp == public_disp:
        upd_disp()
    
    if public_disp == private_list and image_num < 13:
        win_screen = PhotoImage(file='images\win.png')
        display.config(image=win_screen)

    public_word_label.config(text=public_disp)


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
    global playing
    guess = text_var.get().lower()
    if guess != '' and playing:
        if guess not in list_var[26:]:
            list_var += guess
        guess_list.config(text = list_var)
        guess_box.delete(0, tk.END)
        hangman_check(guess)   

def upd_disp():
    """changes the display image"""
    global image_num
    global image_state
    image_num += 1
    image_path = 'images\hangman' + str(image_num) + '.png'
    image_state = PhotoImage(file=str(image_path))
    display.config(image=image_state)
    
def get_priv():
    """takes the private word from the entry box and restarts the game with new priv"""
    global priv_word
    global list_var
    global image_num
    global start_image
    
    #resetting the game
    image_num = 1
    list_var = "You've guessed the letters:\n"
    start_image = PhotoImage(file='images\hangman1.png')
    display.config(image=start_image)

    priv = priv_word.get()
    priv_word_entry.delete(0, tk.END)
    hangman(priv)


#lets the image incriment in a dumb way
image_num = 1

#implimenting the guess box to get data from
text_var = tk.StringVar()
list_var = "You've guessed the letters:\n"

image_start = PhotoImage(file='images\hangman1.png')

#write word button (private)
priv_word = tk.StringVar()
priv_label = ttk.Label(window, text='Enter guessing word below then press the button!')
priv_word_entry = ttk.Entry(window, textvariable=priv_word, )
priv_word_but = ttk.Button(window, text='submit word for guessing (restarts game)', command=get_priv)

priv_label.pack()
priv_word_entry.pack()
priv_word_but.pack()


#adds the image disp and the public disp
public_word_label = ttk.Label(window, text='Input a word to start!')
display = ttk.Label(window, image=image_start)

display.pack()
public_word_label.pack()

# add the letter guessing interface
guess_box = ttk.Entry(window, textvariable=text_var)
guess_but = ttk.Button(window, text='submit guess', command=get_guess)
guess_list = ttk.Label(window, text = list_var)

guess_box.pack()
guess_but.pack()
guess_list.pack()




#think it starts the window idk
window.mainloop()