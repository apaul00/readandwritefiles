import csv

# creates file object
customers = open("customers.csv", "r")

outfile = open("customer_country.csv", "w")

# reads file object of customers, creates CSV object - delimiter seperates values by comma
customer_file = csv.reader(customers, delimiter=",")

# to skip a line if the file contains a header record
next(customer_file)

# advances through each line in file one at a time
count = 1
for record in customer_file:

    outfile.write(record[1] + "," + record[2] + "," + record[4] + "\n")
    count += 1
    # print(type(record))
    # causes pause until keystroke - input()

print("Number of customers:", count)

outfile.close()
