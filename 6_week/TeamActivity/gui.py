'''Team Activity Week 6
'''


import tkinter as tk
from tkinter import *
from tkinter import Frame, Label, Button, ttk
from number_entry import IntEntry, FloatEntry
import math

def main():

    root = tk.Tk()
    root.title('Week 6 Team Activity')
    root.geometry('400x400')

    #My first Notebook
    nb = ttk.Notebook(root)

    #Area of a circle Frame
    pi_formula = ttk.Frame(nb)
    pi_formula.pack(fill=tk.BOTH, expand=True)
    frame1(pi_formula)

    #Area of a rectangle
    rectangle_formula = ttk.Frame(nb)
    rectangle_formula.pack(fill=tk.BOTH, expand=True)
    frame2(rectangle_formula)



    #Add into the notebook our Frames
    nb.add(pi_formula, text="Area of a circle")
    nb.add(rectangle_formula, text='Area of a Rectangle')

    #Show the notbook.
    nb.grid(row=0, column= 0, padx=10, pady=10, sticky='nsew')

    root.mainloop()

def frame1(pi_formula):
    '''This funciton is used to show the labels, textbox and buttons of the 
    programm
    
    Parameters: main_window that means is the root (app) tk.TK()
    
    Return: nothing
    '''
    #Cretae the title of the Formula
    lbl_title = Label(pi_formula, text='Radio of the circle')

    #Create the label to express where type the area
    lbl_radio = Label(pi_formula, text='Radio: ')

    #Label to show the result
    lbl_result = Label(pi_formula, text="")

    #Create an entry box where the user will type the radio:
    ent_radio = FloatEntry(pi_formula)

    #Create the button to calculate the area.
    button_radio = Button(pi_formula, text="Calculate the Radio")
    button_clean = Button(pi_formula, text='Clean')

    #Layout all the lables, entry boxes, and buttons in a grid
    lbl_title.grid(row=0, column=1, padx=10, pady=10, sticky= 'n')
    lbl_radio.grid(row=1, column=0, padx=3, pady=3)
    lbl_result.grid(row=2, column=1, padx=3, pady=3)
    ent_radio.grid(row=1, column=1, sticky='n', padx=3, pady=3)
    button_radio.grid(row=3, column=1, sticky="s", padx=3, pady=3)
    button_clean.grid(row=4, column=1, sticky="s", padx=3, pady=3)

    def calculate_circle_area():
        '''Compute the area of the circle with the user's data 
        '''
        try:
            #Get the area
            area = float(ent_radio.get())
            operator_pi = math.pi

            #Calculation
            result = operator_pi * (area ** 2)

            lbl_result.config(text=f'{result:.2f}')

        except ValueError:
            lbl_result.config(text="")

    def clean():
        '''Clean all'''

        button_clean.focus()
        ent_radio.clear()
        lbl_result.config(text='')

    button_radio.config(command = calculate_circle_area)
    button_clean.config(command = clean)


def frame2(frame2):
    '''This Function will define the second frame of the program
    and will insert labels and entry boxes.

    Paremeters: Main_window that means is the root of the app.

    Return:
    Nothing
    '''
    #First the all labels:
    lbl_title = Label(frame2, text="Are of a rectangle")
    lbl_weight = Label(frame2, text='Weight: ')
    lbl_high = Label(frame2, text='Hight: ')
    lbl_result = Label(frame2, text='Type data')

    #The Entries:
    ent_weight = FloatEntry(frame2)
    ent_high = FloatEntry(frame2)


    #Create de buttons:
    button_calculate = Button(frame2, text='Calculate')
    button_clean = Button(frame2, text='Clean')

    #Layout the all lables, entries boxes and buttons with grid

    lbl_title.grid(row=0, column=1, padx=10, pady=10, sticky= 'n')
    lbl_weight.grid(row=1, column=1, padx=3, pady=3)
    lbl_high.grid(row=2, column=1, padx=3, pady=3)
    lbl_result.grid(row=3, column=2, padx=3, pady=3)
    ent_weight.grid(row=1, column=2, sticky='n', padx=3, pady=3)
    ent_high.grid(row=2, column=2, sticky='n', padx=3)
    button_calculate.grid(row=3, column=1, sticky="s", padx=3, pady=3)
    button_clean.grid(row=4, column=1, sticky="s", padx=3, pady=3)

    def calculate_area_rectangle():
        '''Function to develop the area of the rectangle:'''

        try:
            #get the data

            w = float(ent_weight.get())

            h = float(ent_high.get())

            #Operation:

            result = w * h

            lbl_result.config(text=f'{result:.2f}')

        except ValueError:
            lbl_result.config(text='There is no data')

    def clean():
        '''Clean all'''

        button_clean.focus()
        ent_high.clear()
        ent_weight.clear()
        lbl_result.config(text='')

    button_calculate.config(command = calculate_area_rectangle)
    button_clean.config(command = clean)




if __name__ == "__main__":

    main()