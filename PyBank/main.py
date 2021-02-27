import csv
import os 
from statistics import mean
import math


current_directory = os.path.dirname(__file__)
budget_data = os.path.join(current_directory, "Resources", "budget_data.csv")

with open(budget_data) as handle:

    #specify delimiter and variable in which we will hold contents of file
    reader= csv.reader(handle, delimiter = ',')

    #Read the header row first (skip if there is no header)
    csv_header = next(reader)


    #create list variable to hold months in 
    months = []
    #create list variable to hold profit of each month
    monthProf = []
    #create int variable to hold net total of profits/losses
    total = 0
    #create for-loop that loops through all rows in file
    for row in reader:
        
        months.append(row[0])
       
        #casts the profit as an integer and stores in profLoss
        profLoss = int(row[1])
        monthProf.append(int(row[1]))
        #adds profit of that row to total
        total = total +profLoss



    
    aveCh = list()
    for i in range (85):
        aveCh.insert(i," ")
    
    for j in range(85):
        change =int(monthProf[j+1] - monthProf[(j)])
        aveCh[j]=change
    aveAveCh= (sum(aveCh)/len(aveCh))
    maxCh = max(aveCh)
    minCh= min(aveCh)

    indMax = aveCh.index(maxCh)
    dateMax = (months[(indMax+1)])
    
    
    indMin = aveCh.index(minCh)
    dateMin = (months[(indMin+1)])

    


    #Terminal output 
    print("\nFinancial Analysis\n")
    print("----------------------------")
    print("\nTotal months: "+ str(len(months)))
    #prints total profit
    print("Total profit: " + str(total))
    print("Average Change: " + str(aveAveCh))
    print("Greatest Increase in Profits: " + dateMax + " (" + str(maxCh)+ ")")
    print("Greatest Decrease in Profits: " + dateMin + " (" + str(minCh)+ ")")



    #opens/creats analysis.txt file to write output to
    output_handle = open("analysis.txt","w+")

    output_handle.write("Financial Analysis")
    output_handle.write("\n----------------------------\n")
    output_handle.write("Total Months: " + str(len(months)))
    output_handle.write("\nTotal: " + str(total))
    output_handle.write("\nAverage Change: " + str(aveAveCh))
    output_handle.write("\nGreatest Increase in Profits: " + dateMax + " (" + str(maxCh)+ ")")
    output_handle.write("\nGreatest Decrease in Profits: " + dateMin + " (" + str(minCh)+ ")")


    
