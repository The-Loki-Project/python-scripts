#!/usr/bin/python

import math

# get data
def get_and_validate_talk_time():
    global talk_time
    global plan_type

    # get the minutes
    talk_time = int(input("Enter the number of minutes talked: "))
    while  talk_time not in range(10080):
        #error code
        print('Try Again!\n')
        #prompt again
        talk_time = int(input("Enter the number of minutes talked: "))

    # get the plan type
    plan_type = str(input("Enter the plan type [s, S, r, R, c, C]: "))
    correct_types = ["r","R","c","C","s","S"]
    while plan_type not in correct_types:
        #error code
        print('Try Again!\n')
        #prompt again
        plan_type = str(input("Enter the plan type [s, S, r, R, c, C]: "))

    return talk_time, plan_type

def calculate_talk_time(plan_type, talk_time):
    global amount
    if plan_type == "s" or plan_type == "S": # plan_type in ["s", "S"]
        amount = talk_time * 0.15
    elif plan_type == "c" or plan_type == "C": # plan_type in ["c", "C"]
        # determine the overage and calculate the amount
        if talk_time <= 300:
            amount = talk_time * .20
        elif talk_time >= 300:
            talk_time = talk_time - 300
            amount = talk_time * .10 + 300 * .20
    elif plan_type == "r" or plan_type == "R": # plan_type in ["r", "R"]
        # determine the overage and calculate the amount
        if talk_time <= 120:
            amount = talk_time * .10
        elif talk_time >= 120:
            talk_time = talk_time - 120
            amount = talk_time * .05 + 120 * .10
    else:
        print('Hmmmm something went wrong, try again!')

        # check whether the amount is above the first X minutes
        # if it is, determine the difference and apply the rates to the first X minute nad the second rate to the next X - talk_time
        # if not, calc amt = minute * rate
    return amount

# Function to process customer data
def main():
    global Balance_Amount
    customer_id = input("Enter a Customer ID"

    get_and_validate_talk_time()

    calculate_talk_time(plan_type, talk_time)

    if amount <= 25:
        amount = 25 - amount
        Balance_Amount = ('Remaining Credit:', amount)
    else amount >= 25:
        amount = amount - 25
        Balance_Amount = ('Amount due:', amount - 25)

    return Balance_Amount

print(Balance_Amount)

  
    

