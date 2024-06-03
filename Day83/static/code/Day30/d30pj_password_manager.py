from tkinter import * # only class
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- SEARCH ------------------------------- #
def search():
    website = entry_web.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file) # dict
    except json.decoder.JSONDecodeError:
    # except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}\n")
        else:
            messagebox.showinfo(title="Oops", message="No details for the website exists.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    entry_password.delete(0, "end")
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = ''.join(password_list) # list to string
    # print(f"Your password is: {password}")
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_web.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file) # dict
        except json.decoder.JSONDecodeError:
        # except FileNotFoundError:
            with open("data.json", "w") as file:
                # Writing new data
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as file:
                # Writing Updated data
                json.dump(data, file, indent=4)
        finally:
            entry_web.delete(0, "end") # delete(first, last)
            entry_password.delete(0, "end")
            entry_web.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)

label_passwrod = Label(text="Password:")
label_passwrod.grid(column=0, row=3)

entry_web = Entry(width=29)
entry_web.grid(column=1, row=1)
# entry_web.focus()

entry_email = Entry(width=46)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(END, "yes72002@gmail.com")

entry_password = Entry(width=29)
entry_password.grid(column=1, row=3)

button = Button(text="Search", command=search, width=15)
button.grid(column=2, row=1)

button = Button(text="Generate Password", command=generate_password, width=15)
button.grid(column=2, row=3)

button = Button(text="Add", width=45, command=save)
button.grid(column=1, row=4, columnspan=2)




window.mainloop()