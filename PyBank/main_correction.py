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
with open(pybank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip Header
    next(csvreader)
    
    # Create empty lists to hold the values from the CSV File columns
    date = []
    profits_losses = []

    # Iterate through the rows of the CSV File and append the values from the date column to the empty lists above
    for row in csvreader:
        date.append(row[0])
        profits_losses.append(row[1])
    
    # Calculate total number of months in data set
    total_months = len(date)

    # Calculate the Net Profits/Losses
    # First we must iterate through the datae list and change the data to type of each value to type 'Int' for furture calculations
    for i in range(0, len(profits_losses)):
        profits_losses[i] = int(profits_losses[i])
    
    # make vairable to store the sum of the profits/losses column
    net_total = sum(profits_losses)
    
    # Calculate the Change of Profits/Losses from month to month
    # This must be done using for loop to iterate through profits_losses column and make calculations
    
    # Make empty list for average changes
    average_changes = []
    
    for j in range(1, len(profits_losses)):
        change = (profits_losses[j]) - (profits_losses[j-1])
        average_changes.append(change)
        
    # Zip lists together and create varable to hold the zipped data in a single list for reference
    
    zipped_data = zip(date, profits_losses, average_changes)
    zipped_list = list(zipped_data)
        

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
    print(f"Greatest Increase in Profits: " + (zipped_list[(average_changes.index(max_change))+1][0]) + " (" + '${:.2f}'.format(max_change) + ")")
    print(f"Greatest Decrease in Profits: " + (zipped_list[(average_changes.index(min_change))+1][0]) + " (" + '${:.2f}'.format(min_change) + ")")
    

    # Print Analysis to Text File
    analysis = os.path.join('Analysis', 'Analysis.txt')

    f = open(analysis, "a")
    print("Financial Analysis", file=f)
    print("----------------------------------------------------------------------------------")
    print(f"Total Months: {total_months}", file=f)
    print(f"Total: $" + str(net_total), file=f)
    print(f"Average Change: " + '${:.2f}'.format(avg_rate_change), file=f)
    print(f"Greatest Increase in Profits: " + (zipped_list[(average_changes.index(max_change))+1][0]) + " (" + '${:.2f}'.format(max_change) + ")", file=f)
    print(f"Greatest Decrease in Profits: " + (zipped_list[(average_changes.index(min_change))+1][0]) + " (" + '${:.2f}'.format(min_change) + ")", file=f)
    f.close()