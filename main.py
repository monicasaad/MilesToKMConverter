# import all classes from tkinter module
from tkinter import *

# global variables
FONT = ("Arial", 12)

# create window screen
window = Tk()
window.title("Miles to km Converter")
window.config(padx=20, pady=20)

input = Entry(width=13)
input.insert(END, string="0")
input.grid(row=0, column=1)

conversion = 0

def calculate():
    answer = float(input.get()) * 1.609
    calc_label["text"] = f"{round(answer, 2)}"

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=2)

eq_label = Label(text="is equal to", font=FONT)
eq_label.grid(row=1, column=0)

calc_label = Label(text="0", font=FONT)
calc_label.grid(row=1, column=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(row=1, column=2)

button = Button(text="Calculate", command=calculate) #command function to execute with button click
button.grid(row=2, column=1)



# keep screen open
window.mainloop()
