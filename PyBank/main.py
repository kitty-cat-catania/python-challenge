import csv
import os 
from statistics import mean
import math


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
    #create list variable to hold profit of each month
    monthProf = []
    #create int variable to hold net total of profits/losses
    total = 0
    #create for-loop that loops through all rows in file
    for row in reader:
        #prints ['Month-Year','Profits/Losses']
        print(row)
        months.append(row[0])
       
        #casts the profit as an integer and stores in profLoss
        profLoss = int(row[1])
        monthProf.append(int(row[1]))
        #adds profit of that row to total
        total = total +profLoss
    #prints the length of the array 'months' -- equals 86
    print((len(months)))
    #prints total profit
    print(total)
    print(len(monthProf))
    aveCh = list()
    for i in range (85):
        aveCh.insert(i," ")
    print(len(aveCh))
    for j in range(85):
        change =int(monthProf[j+1] - monthProf[(j)])
        aveCh[j]=change
    print(aveCh)
    print(len(aveCh))
    aveAveCh= (sum(aveCh)/len(aveCh))
    print(aveAveCh)
    maxCh = max(aveCh)
    minCh= min(aveCh)

    print(minCh)
    print(maxCh)

    #opens/creats analysis.txt file to write output to
    output_handle = open("analysis.txt","w+")

    output_handle.write("Financial Analysis")
    output_handle.write("\n----------------------------\n")
    output_handle.write("Total Months: " + str(len(months)))
    output_handle.write("\nTotal: " + str(total))
    output_handle.write("\nAverage Change: " + str(aveAveCh))
    output_handle.write("\nGreatest increase in profits: " + str(maxCh))
    output_handle.write("\nGreatest decrease in profits: "+ str(minCh))


    
