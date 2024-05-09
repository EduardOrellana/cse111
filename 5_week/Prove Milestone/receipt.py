#CopyRight Erick Orellana

'''Receipt.py Prove Milestone First Part
'''

#Libraries we'll be using to develop this assigment.
import os
import csv
from datetime import datetime, date, time
import random


#This variable will ensure that the file we are looking for
#Will be at the same folder.
script_dir = os.path.dirname(os.path.abspath(__file__))


#Read_Dictionary First Function
def read_dictionary(filename, key_column_index = 0):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    #Empty dictionary

    dictionary = {}

    #Open the CSV File with the Function With

    with open(filename, 'rt') as csv_file:

        #insert the csv_file into the module reader

        reader = csv.reader(csv_file)

        #Jump the titles

        next(reader)

        #Read each row to insert the items into the dictionary

        for i_line in reader:

            #Validate if the current line is not blank

            if len(i_line) != 0:

                #Retrieve the data
                #Set the Key of each item
                key = i_line[key_column_index]

                #set the items inside the Key

                dictionary[key] = i_line
    

    #Return the function
    return dictionary

#The index for each column
NAME_INDEX = 1
PRICE_INDEX = 2
PRODUCT_INDEX = 0

def main():
    try:
        # #We are going to provide to the User to upload the file name
        # FILE_NAME = input('Type the csv file: ')

        products_file = os.path.join(script_dir,'products.csv')
        request_file = os.path.join(script_dir,'request.csv')

        DICTIONARY = read_dictionary(products_file)

        # #Printer of the Dictionary
        # for i in DICTIONARY:
        #     print(f'{i} = {DICTIONARY[i]}')


        #Function print to start the list we get from the request.csv file
        print('\nYour Receipt: \n')

        #List to sum the quantities of the request.csv file
        list_quantity = []
        list_subtotal = []
        list_items = []

        #Open the request.csv file for reading
        #req_file is the variable we are going to use for this block  
        with open(request_file, 'rt') as req_file:

            reader = csv.reader(req_file)
            next(reader)

            for i in reader:
                
                #Validate if the line is not blank
                if len(i) != 0:
                    
                    code_product = i[0]
                    quantity = int(i[1])


                    ITEMS = DICTIONARY[code_product]
                    NAME_PRODUCT = ITEMS[NAME_INDEX]
                    PRICE_PRODUCT = float(ITEMS[PRICE_INDEX])
                    CODES = ITEMS[PRODUCT_INDEX]

                    #Price * Quantity
                    price_per_product = quantity * PRICE_PRODUCT

                    #Print the requested items
                    print(f'{NAME_PRODUCT} {quantity} @ {PRICE_PRODUCT}')

                    #Insert the number of quantity to extract the total sum
                    list_quantity.append(quantity)
                    list_subtotal.append(price_per_product)
                    list_items.append(CODES)


        total_sum = sum(list_quantity)
        subtotal = sum(list_subtotal)
        sales_tax = subtotal * 0.06
        net_total = subtotal + sales_tax

        #Exceeding the requirements:
        disc = discount(net_total)

        #To say to the customer that He/She had a discount!

        if disc != 0:
            print(f'\nYou got a discount of {disc:.2f}')

        net_total = subtotal + sales_tax - disc

        print(f'\nNumber of Items: {total_sum} \
                \nSubtotal: {subtotal:.2f} \
                \nSales Tax: {sales_tax:.2f} \
                \nTotal: {net_total:.2f}\n')
        
        #Exceeding Requirements:
        coupon_item = coupon_aleatory(list_items)

        print(f"You'll have a coupon for this item: {coupon_item} Congratulations!and thanks four choosing us! you are always will be welcome!\n")
        
        real_time()

        print()
        
        survey = input('Would you like to help us with a little survey? (yes/not)')

        if survey.lower() != "yes":
            print('Good Bye! We will be waiting for your next visit! ')
        else:
            online_survey()
    
    except FileNotFoundError as file_not_found_error:
        print('\nError: mising file'.upper())
        print(file_not_found_error)

    except KeyError as key_error:
        print('\nError: unkown product ID in the request.csv file'.upper())
        print(key_error)

    except PermissionError as permission_error:
        print('\nSomething is wrong with the permission of the file'.upper())
        print(permission_error)


def real_time():
    """Print the real time when the purchase was made it.

    No Parameters.
    Return: a message with regards
    """

    today = datetime.now()

    message = f"Thanks for your shoping with us at Orellana's Store\n {today:%A, %B %d, %Y - %I:%M %p}\n"

    print(message)

#Exceeding Requirements
def discount(amaunt):
    """Operate and get the total discount if the current day
    is Tuesday or wednesday and also if the curren hour is before
    11:00am

    Parameters:
        Number of the day
    Return: the discount of the purchase.
    """
    current_day = date.isoweekday(date.today())
    current_time = datetime.now().time()
    target_of_time = time(11, 0)
    discount = 0

    if current_day == 2 or current_day == 3:
        discount = amaunt * 0.10

    if current_time < target_of_time:
        discount = discount + (amaunt * 0.10)

    return discount

def coupon_aleatory(dictionary):
    '''This Functions will allow to choose between the items whom will have a coupon.

    Parameters:
        The list of the Items

    Return:
        One item from the List
    '''

    item = random.choice(dictionary)

    return item

def online_survey():
    '''This function contains the entire survey to get information from the customer
    '''

    print('\nPlease rate us (1 to 10) the following questions: \n')
    input('Customer Experience: ')
    input('Storage of the suministers: ')
    input('Clean: ')
    input('Method to pay: ')
    input('Enviroment: ')

    print()
    print('Thanks! now! please leave a little comment, something we can improve and make better: ')
    input('\n\n')
    print('Thanks!!! Have a nice return')



# Call main to start this program.
if __name__ == "__main__":
    store_name = "Orellana's Store"
    print(f'\n{store_name.center(50)}')
    main()
    # print()
    # real_time()