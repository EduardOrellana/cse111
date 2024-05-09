#example 2

import csv
import os

def main():
    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.

    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, "hymns.csv")

    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:
            print(row_list)


# Call main to start this program.
if __name__ == "__main__":
    main()