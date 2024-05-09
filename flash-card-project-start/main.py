from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_TUPLE_LANGUAGE = ("Ariel", 40,"italic")
FONT_TUPLE_WORD = ("Ariel", 60,"bold")

"""Functionality"""
try:
    data = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('./data/french_words.csv')
    word_dict = pd.DataFrame.to_dict(data, orient="records")
else:
    word_dict = pd.DataFrame.to_dict(data, orient="records")



current_card = {}
history = []



def right():
    global current_card
    if len(word_dict) == 0:
        words_to_learn = pd.DataFrame(history)
        words_to_learn.to_csv('words_to_learn.csv')
    else:
        next_card()
        word_dict.remove(current_card)
    
    

def wrong():
    global current_card
    global history
    if len(word_dict) == 0:
        words_to_learn = pd.DataFrame(history)
        words_to_learn.to_csv('words_to_learn.csv')
    else:
        next_card()
        history.append(current_card)
        word_dict.remove(current_card)

def next_card():
    global current_card
    current_card = random.choice(word_dict)
    canvas.itemconfig(language_text, text='French', fill="black")
    canvas.itemconfig(language_word, text=f"{current_card.get("French")}",fil='black')
    canvas.itemconfig(card_background, image=card_front_img)
    window.after(3000, flip_card)
    

def flip_card():
    canvas.itemconfig(language_text, text="English", fill= "white")
    canvas.itemconfig(language_word, text=f'{current_card.get('English')}', fill='white')
    canvas.itemconfig(card_background, image=card_back_img)
    window.after_cancel(flip_card)
    


"""Creating UI"""

window = Tk()
window.title('Flashy')
window.config(bg = BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file='./images/card_front.png')
card_background = canvas.create_image(400,263,image=card_front_img)
canvas.grid(rowspan=2, columnspan=2)

language_text = canvas.create_text(400,150, text="French", fill="black", font=FONT_TUPLE_LANGUAGE)
language_word= canvas.create_text(400,263, text="French_word", fill="black", font=FONT_TUPLE_WORD)




#card_front = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_back_img = PhotoImage(file='./images/card_back.png')
# card_back.create_image(400,263,image=card_back_img)
# card_back.grid(rowspan=2, columnspan=2)


# english_text = card_front.create_text(400,150, text="French", fill="white", font=FONT_TUPLE_LANGUAGE)
# english_word = card_front.create_text(400,263, text="French_word", fill="white", font=FONT_TUPLE_WORD)


wrong_img = PhotoImage(file="./images/wrong.png")
right_img = PhotoImage(file="./images/right.png")


wrong_button = Button(image=wrong_img,command=wrong, bg=BACKGROUND_COLOR, highlightthickness=0)
wrong_button.grid(row=2, column=0)

right_button = Button(image=right_img,command=right, bg=BACKGROUND_COLOR, highlightthickness=0)
right_button.grid(row=2, column=1)







window.mainloop()