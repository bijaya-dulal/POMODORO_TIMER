import tkinter
import math

# ------------------------- constant ------------#

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN =25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
global already_start
already_start = False


# ------------------------- TIMER------------#
def reset_timer():
    global already_start
    already_start = False
    global reps
    reps = 0
    window.after_cancel(timer)
    title_label.config(text="Timer", fg = GREEN)
    check_mark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ------------------------- TIMER MECHANISM ------------#
def start_timer():
    global already_start
    check = already_start
    if(is_already_start(check)):
    
        global reps
        reps += 1
        work_sec = WORK_MIN *60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if reps % 8 == 0 :
            count_down(long_break_sec)
            title_label.config(text="Break", fg=RED)

        elif reps % 2 == 0:
            count_down(short_break_sec)
            title_label.config(text="Break", fg=PINK)

        else:
            count_down(work_sec)
            title_label.config(text="Work", fg=GREEN)

# ------------------------- COUNTDOWN MECHANISM------------#
def count_down(count):
    minute = math.floor(count / 60)
    second = count % 60

    if int(second) < 10:
        second = f"0{second}"

    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        working_session = math.floor(reps/2)
        for _ in range(working_session):
          mark += "√"
        check_mark.config(text = mark)

#------------------- check if already start or not------------# 
def is_already_start(started):
    global already_start
    if(started):
        return False
    else:
        already_start = True
        return True
# ------------------------- UI SETUP ------------#

window = tkinter.Tk()
window.title("pomodoro",)
window.config(pady=30, padx=30, bg=YELLOW)

# title label
title_label = tkinter.Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg= YELLOW)
title_label.grid(row=1, column=2)

canvas = tkinter.Canvas(width=250, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(125, 112, image=tomato_img)
timer_text = canvas.create_text(110, 122, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=2, column=2)

# creating button

start_button = tkinter.Button(text="start", fg="black", highlightthickness=0, command=start_timer)
start_button.grid(row=3, column=1)

reset_button = tkinter.Button(text="reset", fg="black", highlightthickness=0, command=reset_timer)
reset_button.grid(row=3, column=3)

check_mark = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_mark.grid(row=3, column=2)

window.mainloop()
