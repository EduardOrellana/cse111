def main():
    # Get an odometer value in U.S. miles from the user.

    # Get another odometer value in U.S. miles from the user.

    # Get a fuel amount in U.S. gallons from the user.

    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.

    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.

    # Display the results for the user to see.

    start = float(input('Type the Starting adometer value in miles: '))
    end = float(input('Type the ending odometer value in miles: '))
    amount_fuel = float(input('Insert the amount of fuel in gallons: '))

    compute_fuel_efficiency = miles_per_gallon(start,end, amount_fuel)
    compute_lp100k = lp100k_from_mpg(compute_fuel_efficiency)


    print(f'The total in miles per gallon is : {compute_fuel_efficiency:.1f} and per lp100k is {compute_lp100k:.2f}')


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """

    mpg_ = (end_miles - start_miles) / amount_gallons

    return mpg_


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """

    lp_ = 235.215 / mpg

    return lp_


# Call the main function so that
# this program will start executing.
main()