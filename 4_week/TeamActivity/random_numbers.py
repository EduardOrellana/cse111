'''Program activity week 4 Programming with functions
'''

import random

def main():
    numbers = [16.2, 75.1, 52.3]
    print()
    print(numbers)

    append_random_numbers(numbers)
    print(numbers)

    append_random_numbers(numbers, 4)
    print(numbers)

    print('\n\nNOMBERS LISTS')


    words = ['House', 'Car', 'Ball']
    print(f'\n\n{words}')
    append_random_words(words)
    print(words)
    append_random_words(words, 2)
    print(words) 

def append_random_numbers(numbers_list, quantity=1):
    '''Computes quantity pseudo random numbers by calling the random.uniform
    function. Round the quantity pseudo random to one digit after the decimal.
    Appends the quantity psudo random numbers onto the end of the number_list
    '''

    for _ in range(quantity):
        random_number = random.uniform(0,100)
        rounded = round(random_number, 1)
        numbers_list.append(rounded)
        

def append_random_words(words_list, quantity = 1):
    '''Computes and append to the word list
    '''

    words_list_random = ['BYU', 'Book Of Mormon', 'Bible', 'Pday', 'Motocycle', 'Boat', 'Airplane']

    for _ in range(quantity):
        random_word = random.choice(words_list_random)
        words_list.append(random_word)


if __name__ == "__main__":
    main()
