# using the file student_scores.csv calculate the average score of each student
# and save it to a new csv file named student_avg.csv

# 9) student_avg.csv - file that is produced after running step 8

import csv

student = open("Student_Scores.csv", "r")
outfile = open("student_avg.csv", "w")

student_file = csv.reader(student, delimiter=",")

# next(student_file) (skips first line of csv if included)

for record in student_file:

    score_total = float(record[1]) + float(record[2]) + float(record[3])
    average_score = score_total / 3

    outfile.write(str(f"{average_score:<,.2f}") + "\n")
