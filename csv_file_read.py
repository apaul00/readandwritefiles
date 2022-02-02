import csv

# creates file object
customers = open("customers.csv", "r")

# reads file object of customers, creates CSV object - delimiter seperates values by comma
customer_file = csv.reader(customers, delimiter=",")

# to skip a line if the file contains a header record
next(customer_file)

# advances through each line in file one at a time
for record in customer_file:
    print(record[1], record[2])
    # print(type(record))

    # causes pause until keystroke
    input()
