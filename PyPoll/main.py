import csv
import os

curr_dir = os.path.dirname(__file__)
election_data = os.path.join(curr_dir, "Resources", "election_data.csv")

with open(election_data) as dandy:
    read = csv.reader(dandy, delimiter = ',')
    
    header= next(read)

    tot_votes = 0
    unique_cand = []
    khanVotes = 0
    correyVotes= 0 
    liVotes = 0
    otoolVotes = 0
    #loop through all the rows in csv reader
    for row in read:
        tot_votes+=1
        if row[2] not in unique_cand:
            unique_cand.append(row[2])

        if row[2] == "Khan":
            khanVotes +=1
        elif row[2] == "Correy":
            correyVotes +=1
        elif row[2] == "Li":
            liVotes+=1
        elif row[2]== "O'Tooley":
            otoolVotes +=1
    
    Num_khan = ((khanVotes)/tot_votes)
    percent_khan = "{:.0%}".format(Num_khan)
    num_correy = ((correyVotes)/tot_votes)
    percent_correy = "{:.0%}".format(num_correy)

    num_li = ((liVotes)/tot_votes)
    percent_li = "{:.0%}".format(num_li)

    num_otool = ((otoolVotes)/tot_votes)
    percent_otool = "{:.0%}".format(num_otool)

    votes = [khanVotes,correyVotes,liVotes,otoolVotes]
    winnerVotes = max(votes)
    winner = "Khan"

    print("Election Results\n")
    print("----------------------------\n")
    print("Total Votes: " + str(tot_votes))
    print("\n----------------------------\n")
    print("\nKhan: " + str(percent_khan) + " ("+ str(khanVotes)+ ")")
    print("\nCorrey: " + str(percent_correy) + " ("+ str(correyVotes)+ ")")
    print("\nLi: " + str(percent_li) + " ("+ str(liVotes)+ ")")
    print("\nO'Tooley: " + str(percent_otool) + " ("+ str(otoolVotes)+ ")")
    print("----------------------------\n")
    print("Winner: " + str(winner))
    print("\n----------------------------\n")

    output_dandy = open("poll_analysis.txt", "w+")
    output_dandy.write("Election Results\n")
    output_dandy.write("----------------------------\n")
    output_dandy.write("Total Votes: " + str(tot_votes))
    output_dandy.write("\n----------------------------")
    output_dandy.write("\nKhan: " + str(percent_khan) + " ("+ str(khanVotes)+ ")")
    output_dandy.write("\nCorrey: " + str(percent_correy) + " ("+ str(correyVotes)+ ")")
    output_dandy.write("\nLi: " + str(percent_li) + " ("+ str(liVotes)+ ")")
    output_dandy.write("\nO'Tooley: " + str(percent_otool) + " ("+ str(otoolVotes)+ ")")
    output_dandy.write("----------------------------\n")
    output_dandy.write("Winner: " + str(winner))
    output_dandy.write("----------------------------\n")