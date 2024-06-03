from tkinter import * # only class
from tkinter import messagebox
import pandas
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
timer = None
word = None

# ---------------------------- READ FILE ------------------------------- #
# data = pandas.read_csv("data/french_words.csv")
# to dictionary
# to_learn = data.to_dict()
# to_learn = data.to_dict(orient="records")
# print(to_learn)
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")

# ---------------------------- FUNCTION ------------------------------- #
def wrong():
    global timer
    window.after_cancel(timer)
    global word
    if len(to_learn) == 0:
        messagebox.showinfo(title="Wow!", message="Congratulation! You have already learned all words.")
    else:
        word = random.choice(to_learn)
        canvas.itemconfig(card, image=card_front_img)
        canvas.itemconfig(french_title_text, text="French", fill="black")
        canvas.itemconfig(french_word_text, text=word["French"], fill="black")
        timer = window.after(3000, flip_card)

def right():
    wrong()
    to_learn.remove(word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

def flip_card():
    global word
    # word = random.choice(to_learn)
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(french_title_text, text="English", fill="white")
    canvas.itemconfig(french_word_text, text=word["English"], fill="white")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=570, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
card = canvas.create_image(400, 300, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)
french_title_text = canvas.create_text(400, 140, text="French", fill="black", font=(FONT_NAME, 40, "italic"))
french_word_text = canvas.create_text(400, 280, text="", fill="black", font=(FONT_NAME, 60, "bold"))
timer = window.after(3000, flip_card)
wrong()

photo_wrong = PhotoImage(file = "images/wrong.png")
button_wrong = Button(image=photo_wrong, command=wrong, highlightthickness=0)
button_wrong.grid(column=0, row=1)

photo_right = PhotoImage(file = "images/right.png")
button_right = Button(image=photo_right, command=right, highlightthickness=0)
button_right.grid(column=1, row=1)


window.mainloop()