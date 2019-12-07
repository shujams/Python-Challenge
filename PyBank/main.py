# PyBank

# Dependencies

import os
import csv
import pandas as pd


# Files to load and output

bankData = os.path.join('.', 'Resources', 'budget_data.csv') 
postData = os.path.join('.', 'Resources', 'budget_analysis.txt')


#Track the various financial parameters

total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999999999]
total_net = 0

# Read the csv and convert it into a list dictionary

with open(bankData) as financial_data:

    # CSV reader specifies delimiter and variable that holds contents, makes columns based off the delimiter (,)
    csvreader = csv.reader(financial_data)
    
    # Read the header row
    header = next(csvreader)
    
    # Extract the first row to avoid appending to net_change_list
    total_months = total_months + 1

    
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])


    
    #loop through the data
    for row in csvreader:
        
        # track the total
        total_months = total_months + 1
        total_net = total_net + int(row[1])

        
        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
            
    # Calculate the average net change
    net_monthly_avg = sum(net_change_list) / len(net_change_list)
    
    output = (
        f"\nFinancial Analysis\n"
        f"======================\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_net:,.2f}\n"
        f"Average Change: ${net_monthly_avg:,.2f}\n"
        f"Greatest Increase In Profits {greatest_increase[0]}, (${greatest_increase[1]:,.2f})\n"
        f"Greatest Decrease in Profits {greatest_decrease[0]}, (${greatest_decrease[1]:,.2f})\n" 
    )
    
    print(output)
        
with open(postData, "w") as txt_file:
    txt_file.write(output)
        
    

    