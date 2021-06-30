# The data we need to retrive.
#1. The total number of votes cast
#2. A complete list of candidated who recieved votes
#3. The percentage of votes each candidates won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

#importing data from csv
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:


# To do: read and analyze the data here.
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Print each row in the CSV file.
   # for row in file_reader:
    #    print(row)    

# Print the header row.
    headers = next(file_reader)
    print(headers)        