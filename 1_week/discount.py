from datetime import datetime, date

#Set the current day and today
current_day = date.isoweekday(date.today())
# current_day = 1
today = datetime.now()

print(str(today).center(50))

while True:
    print()
    print()

    play = input('Run? (yes/not)')
    
    if play == 'not':
        break

    subtotal = float(input('\n\nPlease enter the subtotal: '))


    if current_day == 2 or current_day == 3:
        
        while subtotal < 50 :
            difference = 50 - subtotal
            print(f'\n\n\nOn tuesday and Wednesday we have a discount since $50.00\n and your purchase is less, you currently total is {subtotal:.2f} \nand you need {difference:.2f}')
            more_purchase = float(input('Please add more items to your purchase'))
            subtotal += more_purchase
        
        disc = subtotal * 0.10
        taxes = disc * 0.06

        total = subtotal + taxes - disc

        print(f'\nDiscount: {disc:.2f}')
        print(f'\nSales tax amount: {taxes:.2f}')
        print(f'\nTotal: {total:.2f}')

    else:
        taxes = subtotal * .06

        total = subtotal + taxes
        
        print(f'\nSales tax amount: {taxes:.2f}')
        print(f'\nTotal: {total:.2f}')

    print('...')
    print('...')
    print('...')