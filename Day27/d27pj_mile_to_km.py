# import tkinter
from tkinter import *

def button_clicked():
    print("I got clicked")
    miles = input.get()
    result = round(float(miles) * 1.609344, 2)
    label_result.config(text=result)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=50, pady=50)

# Entyry
input = Entry(width=10)
input.grid(column=1, row=0)

# Label Miles
label_miles = Label(text="Miles", font=("Arial", 10, "normal"))
label_miles.grid(column=2, row=0)

# Label is equal to
label_equal = Label(text="is equal to", font=("Arial", 10, "normal"))
label_equal.grid(column=0, row=1)

# Label result
# result = str(0)
label_result = Label(text="0", font=("Arial", 10, "normal"))
label_result.grid(column=1, row=1)

# Label Km
label_km = Label(text="Km", font=("Arial", 10, "normal"))
label_km.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)



window.mainloop()
