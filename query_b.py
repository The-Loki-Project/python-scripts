#!/usr/bin/env python3

import csv
from collections import defaultdict

#Open the CSV
with open('employee-sample.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    data = list(reader)

#Create a defaultdict to store division names and their employee counts
division_employee_count = defaultdict(int)

#Iterate through the employee data and count employees in "Transportation" divisions
for employee in data:
    division = employee['Division']
    
    #Check if the division starts with "Transportation"
    if division.startswith('Transportation'):
        division_employee_count[division] += 1

#Print division names and their respective employee counts
for division, count in division_employee_count.items():
    print(f"{division}: {count} employees")
