import math as m

'''
A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping. Write a Python program named boxes.py that asks the user for two integers:

the number of manufactured items
the number of items that the user will pack per box
Your program must compute and print the number of boxes necessary to hold the items. This must be a whole number. Note that the last box may be packed with fewer items than the other boxes.
'''
items_total = float(input('Enter the number of items: '))
items_per_box = float(input('Enter the number of items per box: '))

operation = m.ceil(items_total / items_per_box)

print(f"For {items_total:.0f} items, packing {items_per_box:.0f} in each box, \n you will need {operation:.0f} boxes")


