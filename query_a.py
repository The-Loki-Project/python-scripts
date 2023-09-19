#!/usr/bin/env python3

import csv

##Create function to find an employees department by name
def find_department(employee_name, data):
    for employee in data:
        if employee['Full_Name'] == employee_name:
            return employee['Department']

#Open the CSV
with open('employee-sample.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    data = list(reader)

#Use previously defined function to find department of Jared
johnson_department = find_department('Johnson Jared', data)

#List employees in his department
employees_in_same_department = [employee['Full_Name'] for employee in data if employee['Department'] == johnson_department and employee['Full_Name'] != 'Johnson Jared']

#Print Names
for employee_name in employees_in_same_department:
    print(employee_name)
