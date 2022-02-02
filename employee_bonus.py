import csv

employee = open('EmployeePay.csv', 'r')

employee_file = csv.reader(employee, delimiter = ',')

next(employee_file)

for record in employee_file:
    print('First Name:', record[1])
    print('Last Name:', record[2])
    print('Salary:', record[3])
    bonus = int(record[3]) * float(record[4])
    print('Bonus:', str(bonus))
    total_pay = record[3] + bonus
    print('Total Pay:', total_pay)
    input()

