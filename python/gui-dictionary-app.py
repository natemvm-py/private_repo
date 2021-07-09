from tkinter import *

main_window = Tk()
main_window.configure(bg = '#3d3d3d')
#main_window.geometry('500x220')

# Labels
Header = Label(main_window, text = 'Circumference Calculator', bg = '#3d3d3d', fg = 'white', height = 2, font = 'Arias 20 bold').grid(row = 0, column = 0, columnspan = 4)
Label(main_window, text = 'Get Circumference', bg = '#3d3d3d', fg = 'white', height = 2).grid(row = 1, column = 0)
Label(main_window, text = 'Enter Radius:', bg = '#3d3d3d', fg = 'white').grid(row = 1, column = 1)
Label(main_window, text = 'Get Radius', bg = '#3d3d3d', fg = 'white', height = 2).grid(row = 2, column = 0)
Label(main_window, text = 'Enter Diameter:', bg = '#3d3d3d', fg = 'white').grid(row = 2, column = 1)
Label(main_window, text = 'Get Area', bg = '#3d3d3d', fg = 'white', height = 2).grid(row = 3, column = 0)
Label(main_window, text = 'Enter Radius:', bg = '#3d3d3d', fg = 'white').grid(row = 3, column = 1)
Label(main_window, text = 'Get Diameter', bg = '#3d3d3d', fg = 'white', height = 2).grid(row = 4, column = 0)
Label(main_window, text = 'Enter Radius:', bg = '#3d3d3d', fg = 'white').grid(row = 4, column = 1)
 
# Entries
get_circumference = Entry(main_window, width = 7).grid(row = 1, column = 2)
get_radius = Entry(main_window, width = 7).grid(row = 2, column = 2)
get_area = Entry(main_window, width = 7).grid(row = 3, column = 2)
get_diameter = Entry(main_window, width = 7).grid(row = 4, column = 2)

# Functions
def getCircumference(radius):
    print(round((radius * 2) * 3.14159265359, 5))

def getRadius(diameter):
    return round(diameter / 2, 5)

def getArea(radius):
    return round(3.14159265359 * radius * radius, 5)

def getDiameter(radius):
    return round(2 * radius, 5)

# Calculate Buttons
Button(main_window, text = 'Calculate', command = lambda:getCircumference(get_circumference.get('1.0', 'end'))).grid(row = 1, column = 3)
Button(main_window, text = 'Calculate', command = lambda:getRadius).grid(row = 2, column = 3)
Button(main_window, text = 'Calculate', command = lambda:getArea).grid(row = 3, column = 3)
Button(main_window, text = 'Calculate', command = lambda:getDiameter).grid(row = 4, column = 3)

# Answer Entries
Entry(main_window).grid(row = 1, column = 4)
Entry(main_window).grid(row = 2, column = 4)
Entry(main_window).grid(row = 3, column = 4)
Entry(main_window).grid(row = 4, column = 4)

# Main Loop
main_window.mainloop()
