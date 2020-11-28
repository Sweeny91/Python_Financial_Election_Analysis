# Task is to create a Python script that analyzes the records to calculate each of the following:
# Total number of votes cast
# A complete list of candidates who recieved votes
# The percentage of votes each candidate won
# The winner of the election based on popular vote

# Importing dependencies.
import os
import csv
import numpy

# Variable for the path to my csv file that I want to read.
pypoll_csv = os.path.join('Resources', 'election_data.csv')

# Open csv file and read its contents to the csvreader variable
with open(pypoll_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    
    header = next(csvreader)

    # create empty lists for each parameter for later reference
    voter_id = []
    county = []
    candidate = []

    # for loop iterates through csv file and makes each row a list with each parameter being a different index
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    
    # make variable to store the total number of votes cast (or voters)  
    voters = len(voter_id)

    # make variable to store a list of unique candidates
    uniques = list(numpy.unique(candidate))

    # make variable to hold the number of votes the candidate in the 0th index of my unique list
    w = candidate.count(uniques[0])

    # make variable to find percentage of "w" total votes received.
    per_w = format(round((w/voters)*100),".3f")
    
    # make variable to hold the number of votes the candidate in the 1st index of my UNIQUE list   
    x = candidate.count(uniques[1])

    # make variable to find percentage of "x" total votes received.
    per_x = format(round((x/voters)*100),".3f")
    
    # make variable to hold the number of votes the candidate in the 2nd index of my UNIQUE list
    y = candidate.count(uniques[2])

    # make variable to find percentage of "y" total votes received.    
    per_y = format(round((y/voters)*100),".3f")
    
    # make variable to hold the number of votes the candidate in the 3rd index of my UNIQUE list
    z = candidate.count(uniques[3])

    # make variable to find percentage of "z" total votes received.
    per_z = format(round((z/voters)*100),".3f")

    # make variable to store vote count per unique candidate in key: value pairs (dictionary) 
    # will be later referenced to get maximum value in order to determine winner
    winner = {w:uniques[0],x:uniques[1],y:uniques[2],z:uniques[3]}


    # Print statements for financial analysis
    print("Election Results")
    print("--------------------------------------------")
    print(f"Total Votes: " + str(voters))
    print("--------------------------------------------")
    print(f"{uniques[0]}: {per_w}% ({str(w)})")
    print(f"{uniques[1]}: {per_x}% ({str(x)})")
    print(f"{uniques[2]}: {per_y}% ({str(y)})")
    print(f"{uniques[3]}: {per_z}% ({str(z)})")
    print("--------------------------------------------")
    print(f"Winner: {winner.get(max(winner))}")
    print("--------------------------------------------")
    