from asyncore import write
import csv

customers = open('customers.csv', 'r')
country = open('customer_country.csv', 'w')

customer_file = csv.reader(customers, delimiter = ',')

n = -1

for record in customer_file:
    country.write(record[1] + ',' + record[2] + ',' + record[4] + '\n')
    n += 1

print(n)


    





