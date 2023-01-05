from tkinter import *
from math import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SEC_PER_MIN = 60
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    label_title.config(text="Timer", fg = GREEN)
    label_check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN *SEC_PER_MIN
    short_break_sec = SHORT_BREAK_MIN *SEC_PER_MIN
    long_break_sec = LONG_BREAK_MIN *SEC_PER_MIN
    if reps % 8 == 0:
        count_down(long_break_sec)
        label_title.config(text="Long break", fg = RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_title.config(text="Short break", fg = PINK)
    else:
        count_down(work_sec)
        label_title.config(text="Work", fg = GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    min = floor(count/60)
    sec = count%60
    if sec < 10:
        sec = f"0{sec}"
    # canvas.itemconfig(timer_text, text=count)
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    # canvas.itemconfig(timer_text, text=f"{count}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if floor(reps/2) == 1:
            marks = "✔"
        elif floor(reps/2) == 2:
            marks = "✔✔"
        elif floor(reps/2) == 3:
            marks = "✔✔✔"
        label_check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro") # means tomato in Italian
window.config(padx=100, pady=50, bg=YELLOW) # bg = background

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.pack()
canvas.grid(column=1, row=1)
# count_down(5)

label_title = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg = GREEN, bg = YELLOW)
label_title.grid(column=1, row=0)

label_check_marks = Label(font=(FONT_NAME, 15, "bold"), fg = GREEN, bg = YELLOW)
label_check_marks.grid(column=1, row=3)


button_start = Button(text="Start", command=start_timer, highlightthickness=0)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", command=reset_timer)
button_reset.grid(column=2, row=2)



window.mainloop()