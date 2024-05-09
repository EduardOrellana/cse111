#Assignament 1 week 5

import os
import csv

#detect the root or path of the principal file

#Request the Files'name

def main():
    nameoffile = 'provinces.txt'

    #guarantee the root of the file.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(script_dir, nameoffile)

    provinces_list = read_list(file_name)

    print('\nList before clean it\n')
    print(provinces_list)

    #remove first item
    provinces_list.pop(0)

    #Remoe last item
    provinces_list.pop()

    print()
    print()
    print(provinces_list)


    for i in range(len(provinces_list)):
        if provinces_list[i] == "AB":
            provinces_list[i] = "Alberta"
    
    print(provinces_list)


    count = provinces_list.count("Alberta")

    print(count)

def read_list(file):
    '''Read the content of a text file called provinces.txt into a list and
    return the list. Each element in the lis will contain one line
    of text from the text file.

    Parameter = name of file
    '''
    text_list = []

    with open(file, 'rt') as provinces_file:

        for line in provinces_file:

            clean_line = line.strip()

            text_list.append(clean_line)

    return text_list



# Call main to start this program.
if __name__ == "__main__":
    main()