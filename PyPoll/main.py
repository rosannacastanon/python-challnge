#Import os module and csv reader
import os
import csv

#lists to store data
PyPoll_Data = os.path.join('Resources', 'election_data.csv.csv')

#reading csv file with specified delimiter and variable that holds contents
with open(PyPoll_Data, 'r') as csvfile:
    voteReader = csv.reader(csvfile, delimiter =',')
    
    #skip header row
    next(voteReader)
    
    #create empty dictionaries
    voteCount = {}
    candidatesVotes = {}

    #create a variable to hold vote count
    totalVote = 0
    
    #read through the rows of data after the header
    for row in voteReader:

        #count each vote
        totalVote += 1

        #count votes for each candidate
        if row[2] in voteCount:
            voteCount[row[2]] += 1
        
        else:
            voteCount[row[2]] = 1
    
    #creat variable to hold winner of the vote count
    winnerCount = 0

    #loop through voteCount dictionary for percentage of votes won
    for candidate in voteCount:

        #calc and store candidate vote percentage
        candidatesVotes[candidate] = (voteCount[candidate] / totalVote) * 100

        #determine the winner

        if voteCount[candidate] > winnerCount:
            winnerCount = voteCount[candidate]
            winner = candidate
    
    #create file and export financial analysis
    output_path = os.path.join('Analysis', 'election_results.txt')
    
    with open(output_path, 'w', newline="") as txtfile:
    
        txtfile.write(f'''
    Election Results
    --------------------
    Total votes: {totalVote}
    --------------------\n''')

        print(f'''\nElection Results
    --------------------
    Total Votes: {totalVote}
    --------------------''')


        for candidate, votes in voteCount.items():
            txtfile.write(f'    {candidate}: {candidatesVotes[candidate]:.3f}% ({voteCount[candidate]})\n')
            print(f'''    {candidate}: {candidatesVotes[candidate]:.3f}% ({voteCount[candidate]})''')
        txtfile.write(f'''
    --------------------
    Winner: {winner}
    --------------------''')
        print(f'''
    --------------------
    Winner: {winner}
    --------------------''')

    txtfile.close() 