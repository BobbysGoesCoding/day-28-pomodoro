from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
WIDTH = 200
WIDTH_HALF = 100
HEIGHT = 224
HEIGHT_HALF = 112
rep = 0
checkmarks = ''
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global checkmarks
    global rep
    window.after_cancel(timer)
    canvas.itemconfig(timer_canvas, text='00:00')
    timer_label.config(text='Timer')
    checkmarks = ''
    checkmark.config(text=checkmarks)
    rep = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global rep
    rep += 1
    work = WORK_MIN * 60
    small_break = SHORT_BREAK_MIN * 60
    big_break = LONG_BREAK_MIN * 60
    if rep % 2 == 1:
        countdown(work)
        timer_label.config(text='Work', fg=GREEN)
    elif rep % 8 == 0:
        countdown(big_break)
        timer_label.config(text='Break', fg=RED)
    elif rep % 2 == 0:
        countdown(small_break)
        timer_label.config(text='Break', fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    count_min = math.floor(count/60)
    if count_min == 0:
        count_min = '00'
    elif count_min < 10:
        count_min = f'0{count_min}'
    count_s = count % 60
    if count_s == 0:
        count_s = '00'
    elif count_s < 10:
        count_s = f'0{count_s}'
    canvas.itemconfig(timer_canvas, text=f'{count_min}:{count_s}')
    if count > 0:
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        if rep % 2 == 0:
            global checkmarks
            checkmarks += '✔'
            checkmark.config(text=checkmarks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=WIDTH, height=HEIGHT, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(WIDTH_HALF, HEIGHT_HALF, image=tomato)
timer_canvas = canvas.create_text(WIDTH_HALF, HEIGHT_HALF+20, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(column=1, row=1)

start_button = Button(text='Start', bg=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', bg=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark = Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 13, 'bold'))
checkmark.grid(column=1, row=3)

window.mainloop()
