import os
import csv
import pandas as pd



total = 0

csvpath = os.path.join('.', 'Resources', 'budget_data.csv') #.. back a directory, . current directory
print(csvpath)

#df = pd.read_csv('budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents, makes columns based off the delimiter (,)
    csvreader = csv.reader(csvfile, delimiter=',')
    
    
    print(csvreader)
    
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
      
    for row in csvreader:
        
        #csv_header = next(csvreader)
        months = list(csvreader)
        month_count = len(months)
        print(f"Total months: {month_count}")

        
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents, makes columns based off the delimiter (,)
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        
        
        #csvreader.next()
        #total = sum(int(row[1]))

        total += float(row[1])
        print(total)
 

            
    
    
    