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
pybank_csv = os.path.join('Resources', 'budget_data.csv')

# Specify how to open and read the csv file (could go at the end)
with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)


# Define the function and have it accept the 'bank_data' as  its sole parameter
def PyBank(bank_data):

    # make varibale to reference month column
    months = str(bank_data[0])

    # make variable to refrence profits/losses column
    profits_losses = int(bank_data[1])

    # calculate total number of months in data set
    total_months = len(months) - 1

    # Build loop to iterate through rows of data and calculate the net total profits/losses
    net_total = 0

    for i in range(1, len(profits_losses)):

        # calculate the net total profits and losses over the entire period
        net_total += profits_losses
    
    # Make list that utilizes loop to iterate through rows of data and calculate the average change in profits/losses
    average_changes = []

    for j in range(2, len(profits_losses)):

        # Calculate the change in from month to month and append them to the list above
        change = (profits_losses[j]) - (profits_losses[j-1])
        average_changes.append(change)

    # using this new list calculate the average rate of change, max change, and min change
    avg_rate_change = float(sum(average_changes) / len(average_changes))
    max_change = max(average_changes)
    min_change = min(average_changes)

    # Print statements to print analysis to terminal
    print("Financial Analysis")
    print("----------------------------------------------------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: $" + str(net_total))
    print(f"Average Change: " + '${:.2f}'.format(avg_rate_change))
    print(f"Greatest Increase in Profits: " + '${:.2f}'.format(max_change))
    print(f"Greatest Decrease in Profits: " + '${:.2f}'.format(min_change))



