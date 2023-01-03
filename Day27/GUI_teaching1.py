# import tkinter
from tkinter import *
import playground



# total = playground.add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(playground.add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
# my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label = Label(text="I am a Label", font=("Arial", 24, "italic"))
# my_label.pack(side="left") # **kw
my_label.pack() # **kw

my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
def button_clicked():
    print("I got clicked")
    # my_label.config(text="Button Got Clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entyry
input = Entry(width=10)
input.pack()
# print(input.get())



window.mainloop()

