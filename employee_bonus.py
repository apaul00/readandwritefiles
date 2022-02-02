import csv

employee = open("EmployeePay.csv", "r")

employee_file = csv.reader(employee, delimiter=",")

next(employee_file)

for employee in employee_file:
    salary = float(employee[3])
    bonus = float(employee[4])
    bonus_total = salary * bonus + salary
    print("First Name:", employee[1])
    print("Last Name:", employee[2])
    print("Salary:", f"{salary:<,.2f}")
    print("Bonus:", bonus)
    print("Total pay: $", f"{bonus_total:<,.2f}", sep="")
    input()
