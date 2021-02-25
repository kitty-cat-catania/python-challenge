import csv
import os 


current_directory = os.path.dirname(__file__)
budget_data = os.path.join(current_directory, "Resources", "budget_data.csv")

with open(budget_data) as handle:
    print(handle)

    #specify delimiter and variable in which we will hold contents of file
    reader= csv.reader(handle, delimiter = ',')
    print(reader)

    #Read the header row first (skip if there is no header)
    csv_header = next(reader)
    print(csv_header)


    #create list variable to hold months in 
    months = []
    #create for-loop that loops through all rows in file
    for row in reader:
        #prints ['Month-Year','Profits/Losses']
        print(row)
        months.append(row[0])
    #prints the length of the array 'months' -- equals 86
    print((len(months)))