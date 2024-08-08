from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)
        canvas = Canvas(width=250,height=400, bg=THEME_COLOR, highlightthickness=0)
        canvas.grid(column=1,row=2, columnspan=2)

        #Label
        score_label = Label(text="Score:", font=("Arial",12,"bold"))
        score_label.grid(column=2,row=0)

        question_box = Canvas(width=300,height=300, bg="#ffffff", highlightthickness=0)
        question_box.grid(column=1,row=1)
        true_img = PhotoImage(file="day-34/images/true.png")
        false_img = PhotoImage(file="day-34/images/false.png")
        canvas.create_image(62.5,80,image=true_img)
        canvas.create_image(187.5,80,image=false_img)


        self.window.mainloop() 