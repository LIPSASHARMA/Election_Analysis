import os
import csv

# PROJECT OBJECTIVES: 
# Total number of votes cast
# A complete ist of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won 
# The winner of the election based on popular vote


# Assign a variable for the file to load and the path.
# file_to_load = 'Resources\election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file
with open(file_to_load) as election_data:
     # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)
        #print(row[0])
    #    for i in range(len(row)):
    #     print(row[i])
        # Read and print the header row.
    headers = next(file_reader)
    print(headers)




# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    #txt_file.write("Hello World")
    # Write three counties to the file.
    #txt_file.write("Arapahoe, Denver, Jefferson")
    #txt_file.write("Arapahoe\nDenver\nJefferson")

