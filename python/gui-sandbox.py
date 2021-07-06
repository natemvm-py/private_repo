from tkinter import *

main_window = Tk()

# Labels
my_name = Label(main_window, text = 'Name?').grid(row = 0, column = 0)

age = Label(main_window, text = 'Age?').grid(row = 1, column = 0)

# Text Input
Entry(main_window, width = 50, borderwidth = 5).grid(row = 0, column = 1)

Entry(main_window, width = 50, borderwidth = 5).grid(row = 1, column = 1)

def on_click():
    print('My Name is', my_name.get(),'and I am', age.get())

# Button
Button(main_window, text = 'Click Me!', command = on_click).grid(row = 2, column = 1)

main_window.mainloop()