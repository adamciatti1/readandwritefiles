import csv

employee = open('EmployeePay.csv', 'r')

employee_file = csv.reader(employee, delimiter = ',')

next(employee_file)

for record in employee_file:
    print('First Name:', record[1])
    print('Last Name:', record[2])
    print('Salary:', record[3])
    bonus = int(record[3]) * float(record[4])
    print('Bonus:', format(str(bonus), '.2'))
    total_pay = int(record[3]) + float(bonus)
    print('Total Pay:', total_pay)
    input()

