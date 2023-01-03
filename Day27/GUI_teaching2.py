# import tkinter
from tkinter import *

def button_clicked():
    print("I got clicked")
    # my_label.config(text="Button Got Clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200) # padding

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack()
my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


# Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

button_new = Button(text="New Button", command=button_clicked)
button_new.grid(column=2, row=0)

# Entyry
input = Entry(width=10)
# print(input.get())
# input.pack()
input.grid(column=3, row=2)




window.mainloop()
