# Task is to create a Python script that analyzes the records to calculate each of the following:
# Total number of months included in the dataset
# The net total amount of "profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount)
# The greatest decrease in losses (date and amount)

# Import Modules
import os
import csv

# Path to collect data from resources folder
pybank.csv = os.path.join('..', 'Resources', "'budget_data.csv')

# Define the function and have it accept the 'wrestler_data' as  its sole parameter
def PyBank(bank_data):

    # make varibale to reference month column
    months = str(bank_data[0])

    # make variable to refrence profits/losses column
    profits = int(bank_data[1])

    # calculate total number of months in data set
    total_months = len(months)

    print(f"The total number of months in the data set is {total_months}")

    # calculate the net total profits and losses over the entire period
    # first make and initialze net profits/losses variables
    net_profit = 0
    net_loss = 0

    # then construct the conditonal to calculatee the total net profits/losses 
    if profits > 0:
        net_profit += profits
    else: 
        net_loss += profits

    print(f"The total net profit over the period is {net_profit}")
    print(f"The total net loss over the period is {net_loss}")

    # make a varibale for the net total to link ta a conditional in order to distinguise losses from profits
    net_total = net_profit + net_loss

    if net_total > 0:
        print(f"The company gained an amount of ${net_total} over the period!")
    else:
        print(f"The company lost an amount of ${net_total} over the period!")

    # find the average of those changes

    # find the greatest increase in profits

    # find the greatest decrese in profits

        
    


