from tkinter import *
import math
import os

#Variables
expression = ''

#Main Window Creation
main_window = Tk()
main_window.title('Calculator')
main_window.configure(background = '#17202A')
#main_window.geometry('350x500')
main_window.resizable(False, False)

equation = StringVar()
expression_field = Entry(main_window, textvariable = equation)

#Functions
def button_press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


#Labels
#Label(main_window, background = '#17202A', height = 10, width = 45).grid(row = 0, columnspan = 4)
expression_field(background = '#17202A', height = 10, width = 45).grid(row = 0, columnspan=4)

#Buttons - Numbers (0 - 9)
Button(main_window, background = '#212F3D', foreground = 'white', text = '1', height = 5, width = 10).grid(row = 1, column = 0)
Button(main_window, background = '#212F3D', foreground = 'white', text = '2', height = 5, width = 10).grid(row = 1, column = 1)
Button(main_window, background = '#212F3D', foreground = 'white', text = '3', height = 5, width = 10).grid(row = 1, column = 2)
Button(main_window, background = '#212F3D', foreground = 'white', text = '4', height = 5, width = 10).grid(row = 2, column = 0)
Button(main_window, background = '#212F3D', foreground = 'white', text = '5', height = 5, width = 10).grid(row = 2, column = 1)
Button(main_window, background = '#212F3D', foreground = 'white', text = '6', height = 5, width = 10).grid(row = 2, column = 2)
Button(main_window, background = '#212F3D', foreground = 'white', text = '7', height = 5, width = 10).grid(row = 3, column = 0)
Button(main_window, background = '#212F3D', foreground = 'white', text = '8', height = 5, width = 10).grid(row = 3, column = 1)
Button(main_window, background = '#212F3D', foreground = 'white', text = '9', height = 5, width = 10).grid(row = 3, column = 2)
Button(main_window, background = '#212F3D', foreground = 'white', text = '0', height = 5, width = 10).grid(row = 4, column = 1)
#Buttons - Operators (+, -, x, ÷, =, ., ², (), %)
Button(main_window, background = '#212F3D', foreground = 'white', text = '+', height = 5, width = 10).grid(row = 1, column = 3)
Button(main_window, background = '#212F3D', foreground = 'white', text = '-', height = 5, width = 10).grid(row = 2, column = 3)
Button(main_window, background = '#212F3D', foreground = 'white', text = 'x', height = 5, width = 10).grid(row = 3, column = 3)
Button(main_window, background = '#212F3D', foreground = 'white', text = '÷', height = 5, width = 10).grid(row = 4, column = 3)
Button(main_window, background = '#212F3D', foreground = 'white', text = '=', height = 5, width = 10).grid(row = 5, column = 3)
Button(main_window, background = '#212F3D', foreground = 'white', text = '%', height = 5, width = 10).grid(row = 4, column = 2)
Button(main_window, background = '#212F3D', foreground = 'white', text = '.', height = 5, width = 10).grid(row = 4, column = 0)
Button(main_window, background = '#212F3D', foreground = 'white', text = 'a²', height = 5, width = 10).grid(row = 5, column = 0)
Button(main_window, background = '#212F3D', foreground = 'white', text = '(', height = 5, width = 10).grid(row = 5, column = 1)
Button(main_window, background = '#212F3D', foreground = 'white', text = ')', height = 5, width = 10).grid(row = 5, column = 2)

#Main Loop
main_window.mainloop()