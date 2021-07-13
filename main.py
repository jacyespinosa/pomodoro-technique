from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    global reps
    '''
    Convert the input into minutes (count_min) using the math module and also convert the input into seconds
    (count_sec). These variables will be used to display as texts on the canvas (e.g. 25:00).
    '''
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, countdown, count-1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_photo = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_photo)
timer_text = canvas.create_text(106, 130, text='00:00', fill='white', font=(FONT_NAME, 30))
canvas.grid(column=2, row=1)

timer_label = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, 'bold'))
timer_label.grid(column=2, row=0)

start_button = Button(text='Start', bg=YELLOW, highlightthickness=0, command="")
start_button.grid(column=1, row=4)

reset_button = Button(text='Reset', bg=YELLOW, highlightthickness=0, command="")
reset_button.grid(column=3, row=4)

check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'bold'))
check_label.grid(column=2, row=5)

window.mainloop()
