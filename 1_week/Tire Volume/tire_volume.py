import math
import os
from datetime import date
from time import sleep

#Milestone of the week Tire Volume

#My variables
current_date_and_time = date.today()
volume = 0
pi = math.pi

#Creation of the file text at the same folder
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'volumes.txt')
price = float(0)


#I'd like to work with functions I read again my note of the CSE 110 Class
#Functions.
def volume_function (w,r,d):
    w = width
    r = a_ratio
    d = diameter
    volume = round(pi * (w ** 2) * r * ((w * r) + (2540 * d)) / 10000000000)
    return volume

def phone_function ():
    phone_number = int(input('Enter your phone number to confir the purchase: '))
    return phone_number

def print_center(impresion):
    return print(f'{impresion}'.center(30))

#Here is the program body
while True:
    sleep(1)
    print('\nWelcome to the best store of tires!'.upper().center(50))
    print('\n\nEnter this indicator to quote your tires.'.capitalize().center(25))

    width = float(input("\n\nEnter the width of the tire in mm (ex 205): "))
    a_ratio = float(input("\nEnter the aspect ratio of the tire (ex 60): "))
    diameter = float(input("\nEnter the diameter of the wheel in inches (ex 15): "))

    if width == 225 and a_ratio == 65 and diameter == 17:
        price = 99.00
    elif width == 275 and a_ratio == 55 and diameter == 20:
        price =  169.00
    elif width == 205 and a_ratio == 55 and diameter == 16:
        price = 48.95
    elif width == 245 and a_ratio == 55 and diameter == 19:
        price = 115.34
    elif width == 235 and a_ratio == 45 and diameter == 18:
        price = 69.00
    elif width == 235 and a_ratio == 85 and diameter == 16:
        price = 127.00
    else:
        price = 150.00

    print(f'\n\n The price to pay would be ${price:.2f}')
    ensurance = input('\n\nAre you sure about your purchase? (yes/not) ')

    if ensurance == 'yes':
        print('\n\n')
        vol = volume_function(width, a_ratio, diameter)
        phone_num = phone_function()
        with open(file_path, 'at') as volume_file:
            print(f'{current_date_and_time}, {width:.0f}, {a_ratio:.0f}, {diameter:.0f}, {vol}, {phone_num}', file = volume_file)

        print('\n\nHere we show you the details of your purchase: ')

        sleep(0.5)
        
        print('\nWidht: ')
        print_center(width)
        
        sleep(0.5)
        
        print('\nRatio: ')
        print_center(a_ratio)
        
        sleep(0.5)
        
        print('\nDiameter: ')
        print_center(diameter)
    
        sleep(0.05)

        print('\nAnd the volume it is:')
        print_center(vol)

        print('\n\nThanks for your purchase'.center(25))
        break
    else:
        sleep(2)
        print('\n\n\nPlease repeat this: \n\n\n\n'.center(50), flush= True)
