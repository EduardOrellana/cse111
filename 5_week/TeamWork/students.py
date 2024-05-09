#Copyright @Erick Orellana

'''Week 5 Team Activity---
students.csv
As a team, write a Python program named students.py that has at least two functions named main and read_dictionary. 
You must write the read_dictionary function with one of the following two headers and documentation strings. 
Choose the header that makes the most sense to you.
'''
import os
import csv

I_NUMBER_INDEX = 0
NAME_INDEX = 1

def read_dictionary(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """

    dictionary = {}
    #Open a file 
    with open(filename, 'rt') as stuents_file:

        #reader module for the file lecture
        reader = csv.reader(stuents_file)

        #Jump the headers
        next(reader)

        #For loop to go through the csv file
        for i in reader:
            
            #validate if the current line is not blank
            if len(i) != 0:
                
                key = int(i[0])
                value = i[1]

                #insert inside the dicitonary

                dictionary[key] = value

    #Return the function
    return dictionary


#Principal Function:
def main():
    
    script_dir = os.path.dirname(os.path.abspath(__file__))

    #Try block to handle errors

    while True:
        try:
            
            file = os.path.join(script_dir, "students.csv")

            file_dictionary = read_dictionary(file)

            #Next variables we are goint to clean the INumber
            USER_INPUT = input('\n\nType an I-Number of the student: ')

            USER_INPUT = USER_INPUT.replace("-", "")

            USER_INPUT = USER_INPUT.replace(" ", "")


            #This part of the code will ensure that the caracthers will be 9

            if len(USER_INPUT) < 9:
                print('Invalid I-Number: too few digits')
            elif len(USER_INPUT) > 9:
                print('Invalid I-Number: too many digits')
            else:
                #Convert the Key to an integer to seek inside the dictionary
                IdNUMBER = int(USER_INPUT)

                USER_FOUND = file_dictionary[IdNUMBER]

                print(f'The Student is: {USER_FOUND}')

                break
        
        except ValueError as val_err:
            print(f'The value is not a validate value {val_err}')
        
        except KeyError as key_error:
            print("\nInvalid I-Number")



    
#Call main to start this program.
if __name__ == "__main__":
    main()