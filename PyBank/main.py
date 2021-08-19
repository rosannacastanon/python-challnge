import os

import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

total_months = 0
total_net = 0
net_change_list =[]
max_increase = 0
max_decrease = 0

# Method 2: Improved Reading using CSV module


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        change = int(row[1])- last_net
        last_net = int(row[1])
        net_change_list.append(change)

        max_increase = max(net_change_list)
        max_decrease = min(net_change_list)
       
averagechange = round(sum(net_change_list) / len(net_change_list) , 2)

# Print Analysis
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${averagechange}")
print(f"Greatest Increase in Profits:, (${max_increase})")
print(f"Greatest Decrease in Profits:, (${max_decrease })")
