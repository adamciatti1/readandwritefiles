import csv

student_scores = open('Student_Scores.csv', 'r')
student_avg = open('student_avg.csv', 'w')

score_file = csv.reader(student_scores, delimiter = ',')

for record in score_file:
    total = int(record[1]) + int(record[2]) + int(record[3])
    average = int(total) / 3
    student_avg.write(str(record[0]) + ', ' + str(average) + '\n')