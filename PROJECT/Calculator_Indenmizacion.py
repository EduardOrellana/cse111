#Copyright ErickOrellana 2024-Project CSE111

#The all functions to import

from datetime import date, datetime
import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import *
import tkinter.ttk as ttk
from tkinter.simpledialog import askstring
import csv

#My principal window

def show_message(result):
    msgbox.showinfo("Message", f"Hello! to your favorite calculator please help us with the follow data: {result}")


def main():

    #Ask String and Welcome
    name = askstring('Input', 'Enter you name')

    show_message(name)
    
    base_salary = askstring('Input', 'What is your Base Salary: ')
    DATE_ONE = askstring('Input', 'What is your start Date? please follow the next format (YYYY-MM-DD)')
    DATE_TWO = askstring('Input', 'What is your last Date? Same format please (YYYY-MM-DD)')
    VACATIONS_FROM_USER = askstring('Input', 'How Many Vacations do you have? (0-30)')
    
    root = tk.Tk()
    root.title('Project Erick Orellana')
    root.geometry('500x400')

    ttk.Label(root,text='Winter 2024 - Erick Orellana Program', padding=(5, 5)).pack(side='top', fill='x')

    ttk.Label(root,text=f'').pack()
    ttk.Label(root,text=f'Welcome {name} to your favorite Calculator').pack()
    ttk.Label(root,text=f'').pack()
    
    #The notebook, where I will put my Frames each frame will be different calculator
    nb = ttk.Notebook(root)

    #Frame1 Compensation Calculator
    frame1_compensation_calculator = ttk.Frame(nb)
    frame2_vacations_payment = ttk.Frame(nb)
    frame3_total_to_pay = ttk.Frame(nb)


    #Areas of the frame on this time I'm using the method pack()
    frame1_compensation_calculator.pack(fill=tk.BOTH, expand=True)
    frame1(frame1_compensation_calculator, base_salary, DATE_ONE, DATE_TWO)
    COMPENSATION = frame1(frame1_compensation_calculator, base_salary, DATE_ONE, DATE_TWO)
    # print(COMPENSATION)

    frame2_vacations_payment.pack(fill=tk.BOTH, expand=True)
    frame2(frame2_vacations_payment, base_salary, DATE_TWO, VACATIONS_FROM_USER)
    VACATIONS = frame2(frame2_vacations_payment, base_salary, DATE_TWO, VACATIONS_FROM_USER)
    # print(VACATIONS)

    frame3_total_to_pay.pack(fill=tk.BOTH, expand=True)
    frame3(frame3_total_to_pay, name, COMPENSATION, VACATIONS)
    


    #Add into the notebook our frames
    nb.add(frame1_compensation_calculator, text='Compensation Calculator')
    nb.add(frame2_vacations_payment, text='Vacations Calculator')
    nb.add(frame3_total_to_pay, text='Total')

    #Show and Call the notebook
    nb.pack()

    #To call all.
    ttk.Label(root, text='@Copyright Erick Orellana Calculator - 2024').pack(side='bottom', fill='x')
    root.mainloop()

def frame1(frame1_compensation_calculator, base_salary, date_one, date_two):
    '''This Function will return the fram with labels, entry boxes, 

    Parameter:
    '''

    #Set the all labels:
    lbl_base_salary = Label(frame1_compensation_calculator, text= 'Base Salary')
    lbl_Start_date = Label(frame1_compensation_calculator, text= 'Start Date: (YYYY-MM-DD)')
    lbl_end_date = Label(frame1_compensation_calculator, text= 'End Date: (YYYY-MM-DD)')
    lbl_total_days = Label(frame1_compensation_calculator, text='Days: ', background='red')
    lbl_total_money = Label(frame1_compensation_calculator, text='Money: ', background='red')

    #Entry Boxes and Dates
    ent_base_salary = Entry(frame1_compensation_calculator, bd=3)
    ent_start_date = Entry(frame1_compensation_calculator, bd=3)
    ent_end_date = Entry(frame1_compensation_calculator, bd=3)

    #Button to calculate and clear
    button_cal = Button(frame1_compensation_calculator, text='Calculate')
    button_clear = Button(frame1_compensation_calculator, text='Clear All')


    #Layout
    lbl_base_salary.grid(row=0, column=0, padx=10, pady=10)
    lbl_Start_date.grid(row=1, column=0, padx=10, pady=10)
    lbl_end_date.grid(row=2, column=0, padx=10, pady=10)
    ent_base_salary.grid(row=0, column=1, padx=10, pady=10)
    ent_start_date.grid(row=1, column=1, padx=10, pady=10)
    ent_end_date.grid(row=2, column=1, padx=10, pady=10)
    lbl_total_days.grid(row=3, column=0, padx=10, pady=10)
    lbl_total_money.grid(row=3, column=1, padx=10, pady=10)

    button_cal.grid(row=4, column=0, padx=10, pady=10)
    button_clear.grid(row=4, column=3, padx=10, pady=10)

    #Set by defaul the base salary and the dates
    ent_base_salary.insert(0,base_salary)
    ent_start_date.insert(0,date_one)
    ent_end_date.insert(0,date_two)

    '''This variables are calling to set the input that the user
    will insert inside each entry'''

    def button_calculate_frame1():
        '''This Function will compute the button calculte to set the money and Days
        '''

        SALARY = ent_base_salary.get()
        SALARY = float(SALARY)
        DATE_START = ent_start_date.get()
        DATE_END = ent_end_date.get()

        DAYS = daysbetween(DATE_START, DATE_END)

        #This Compensation is the total we have inside the frame1
        COMPENSATION_calculate = compensation_salary(DAYS, SALARY)

        lbl_total_days.config(text=f'Total Days = {DAYS}', background='green', fg='white')
        lbl_total_money.config(text=f'Total in money = {COMPENSATION_calculate:.2f}', background='green', fg='white')

        return COMPENSATION_calculate


    def clear():
        '''The cleaner to reset and start again the calculator
        Parameters: Nothing
        Return: Nothing
        '''
        button_clear.focus()
        ent_base_salary.delete(0, 'end')
        ent_end_date.delete(0, 'end')
        ent_start_date.delete(0, 'end')
        lbl_total_days.config(text="Days: ", background="red", fg='white')
        lbl_total_money.config(text="Money: ", background='red', fg='white')



    COMPENSATION = button_calculate_frame1()

    button_cal.config(command=button_calculate_frame1)
    button_clear.config(command=clear)

    return COMPENSATION


'''Frame 2 it going to be use to show and calculate the vacations payment.'''
def frame2(frame, base_salary, date_two, VACATIONS):
    '''This Function will return the fram with labels, entry boxes, 

    Parameter:
    '''

    #Set the all labels:
    lbl_base_salary = Label(frame, text= 'Base Salary')
    lbl_total_days = Label(frame, text='Total of Vacations ')
    lbl_end_date = Label(frame, text="Last Date ")
    lbl_total_money = Label(frame, text='Money: ', background='red', fg='white')

    #Entry Boxes and Dates
    ent_base_salary = Entry(frame, bd=3)
    ent_end_date = Entry(frame, bd=3)
    ent_total_vacations = Entry(frame, bd=3)

    #Button to calculate and clear
    button_cal = Button(frame, text='Calculate')
    button_clear = Button(frame, text='Clear All')

    #Layout
    lbl_base_salary.grid(row=0, column=0, padx=10, pady=10)
    ent_base_salary.grid(row=0, column=1, padx=10, pady=10)
    lbl_end_date.grid(row=1, column=0, padx=10, pady=10)
    ent_end_date.grid(row=1, column=1, padx=10, pady=10)
    ent_total_vacations.grid(row=2, column=1, padx=10, pady=10)
    lbl_total_days.grid(row=2, column=0, padx=10, pady=10)
    lbl_total_money.grid(row=3, column=1, padx=10, pady=10)

    button_cal.grid(row=4, column=0, padx=10, pady=10)
    button_clear.grid(row=4, column=3, padx=10, pady=10)

    #Set by defaul the base salary and the dates
    ent_base_salary.insert(0,base_salary)
    ent_end_date.insert(0,date_two)
    ent_total_vacations.insert(0, VACATIONS)

    '''This variables are calling to set the input that the user
    will insert inside each entry'''

    def button_calculate_frame2():
        '''This Function will compute the button calculte to set the money and Days
        '''

        SALARY = ent_base_salary.get()
        SALARY = float(SALARY)
        ENDDATE = ent_end_date.get()
        VACATIONS = ent_total_vacations.get()
        VACATIONS = float(VACATIONS)

        DAYS = days_to_vacations(ENDDATE)
        DAYS = float(DAYS)
        
        VACATIONS_PAY = vacations_payment(DAYS, SALARY, VACATIONS)

        lbl_total_money.config(text= f'Total in money = {VACATIONS_PAY:.2f}', background='green', fg='white')

        return VACATIONS_PAY


    def clear():
        '''The cleaner to reset and start again the calculator
        Parameters: Nothing
        Return: Nothing
        '''
        button_clear.focus()
        ent_base_salary.delete(0, 'end')
        ent_end_date.delete(0, 'end')
        lbl_total_money.config(text="Money: ", background='red', fg='white')


    VACATIONS_to_return = button_calculate_frame2()

    button_cal.config(command=button_calculate_frame2)
    button_clear.config(command=clear)

    return VACATIONS_to_return


def daysbetween(start_date, end_date):
    '''This Function will compute and discover how many days there are between
    the start date and end date
    Parameters:
        Start Date
        End Date
    
    Return: Days
    '''
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        #Days between the dates

        difference = end_date - start_date
        
        return difference.days
    
    except ValueError as error:
        print(error)
        print('the Formats of the dates are wrong')
    except:
        print('Please verify the data is correct.')
    else:
        print('One Error has passed, please verify your values')



def days_to_vacations(end_date):
    '''This Function will calculate how many days of the year
    have passed until the given end_date.

    Parameters: 
        end_date: The end date in the format 'YYYY-MM-DD'
        
    Returns:
        Days passed in the current year until the end_date.
    '''
    try:
        #Current Year
        CURRENT_YEAR = date.today().year

        #Crete or extract the first year of the year
        start_date = date(CURRENT_YEAR, 1, 1)

        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

        # Calculate the difference in days between the start date and the end date
        difference = end_date - start_date
        
        return difference.days + 1
    
    except ValueError as error:
        print('Error with the function days for vacations')
        print(error)


def compensation_salary(days, salary):
    '''This Function will compute the total of compensation.
        This Formula works with the total of days but first will
        Compute total salaries per month (14 salaries per year)
        Total of the months
        Salary multiply by 14 (Salaries per year)
        and then divide by 12 (Months)
        and then divide by 365 (year's day)
        and then mulpiply by the datys worked
    
        Parameters: Total Days worked
                    Base Salary

        Return: Compensation
    '''

    message_error = 'ERROR WITH THE FUNCTION COMPESATION SALARY'
    try:

        total_of_salaries = 14
        Months = 12
        salary_by_total_salaries = (salary * total_of_salaries) / Months
        salary_by_total_salaries = salary_by_total_salaries /365
        total = salary_by_total_salaries * days

        return total

    except ValueError:

        print(ValueError)
        print(message_error)

    except ZeroDivisionError:
        print(message_error)
        print(ZeroDivisionError)

    except:
        print('Please verify the data is correct.')


    
def vacations_payment(days, salary, total_of_vacations):
    '''This Function will calculate the total salary per vacations days.
    Paremeters: Days, Salary

    Return: Total to pay ofr vacations
    '''
    try:
        Salary_calculate = (salary * 12) / 365
        vacations_calculate = (days * total_of_vacations) / 365

        RESULT = Salary_calculate * vacations_calculate

        #Result of the function
        return RESULT
    
    except ValueError as error:
        print('something wrong with the function of the vacations please verify the data')
        print(error)

def frame3(frame, name, compensation, vacations):
    '''This Function will show the frame of the total to present to user
    What total He/She will get.

    Parameters: 
        Compensation
        vacations (total)
    
    Return:
        Nothing
    '''
    TOTAL = compensation + vacations

    #Set the labels 
    ent_name = Entry(frame)
    lbl_text_salary = Label(frame, text="Total: ", bg="grey")
    lbl_text_vacations = Label(frame, text="Total in Vacations: ", bg="grey")
    lbl_compensation = Label(frame, text= f'{compensation:.2f}', bg="white", font="bond")
    lbl_vacations = Label(frame, text= f'{vacations:.2f}', bg="white", font="bond")
    ent_total = Entry(frame)

    #insert the results into the entrys
    ent_name.insert(0, str(name))
    ent_name.config(state="disabled")
    ent_total.insert(0, str(TOTAL))
    ent_total.config(state="disabled")

    # #Button to save
    # button_save = Button(frame, text="Save", command=savedintocsv)

    #Grid layout
    ent_name.grid(row= 0, column= 3, padx=10, pady=10)
    lbl_text_salary.grid(row=0, column=0, padx=10, pady=10)
    lbl_text_vacations.grid(row=1, column=0, padx=10, pady=10)
    lbl_compensation.grid(row=0, column=1, padx=10, pady=10)
    lbl_vacations.grid(row=1, column=1, padx=10, pady=10)
    # button_save.grid(row=4, column=3)
    ent_total.grid(row=2, column=3)


    # def savedintocsv():
    #     '''This function will sabe the last result into a CSV File
        
    #     Parameters:
    #         none
    #     Return: 
    #         A csv file
    #     '''
    #     #The fields
    #     NAME = ent_name.get()
    #     TOTAL = ent_total.get() 

    #     #Use a with block to export the results 
    #     with open('compensation.csv', 'w', newline='') as file:
    #         writer = csv.writer(file)
    #         field = ['name', 'total']

    #         writer.writerow(field)
    #         writer.writerow([NAME], [TOTAL])
    

    #I tried to insert one more function to saved the data into a csv file, but 
    #I couldn't I did my best.

if __name__ == "__main__":
    main()
