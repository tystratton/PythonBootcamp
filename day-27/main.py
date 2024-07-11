from tkinter import *

#Window
window = Tk()
window.title("My first GUI Program")
window.minsize(width=500,height=300)

#Label
miles_label = Label(text="Miles", font=("Arial",12,"bold"))
miles_label.grid(column=2,row=0)


is_equal_label = Label(text="is equal to", font=("Arial",12,"bold"))
is_equal_label.grid(column=0,row=1)

km_label = Label(text="0", font=("Arial",12,"bold"))
km_label.grid(column=1,row=1)

#Button
def button_clicked():
    miles = float(input.get())
    print(miles)
    km = miles * 1.60934
    print(km)
    km_label.config(text=km)
    
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1,row=2)

#Entry
input = Entry(width=10)
input.grid(column=1,row=0)

window.mainloop() #keeps windows on screen, and listens

