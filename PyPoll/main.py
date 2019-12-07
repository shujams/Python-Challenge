# PyPoll

# Dependencies

import os
import csv
import pandas as pd


# Files to load and output
electionData = "./Resources/election_data.csv" #.. back a directory, . current directory
postData = os.path.join('.', 'Resources', 'election_analysis.txt')

# Open the CSV
election_data_pd = pd.read_csv(electionData)


#Calculate total votes and votes per candidate
total_votes = len(election_data_pd["Voter ID"].unique())
candidate_votes = election_data_pd["Candidate"].value_counts()


# Convert the voting data into a DataFrame
election_data_df = pd.DataFrame(candidate_votes)
election_data_df.head()


# Rename the "Candidate" and "Vote Count" columns for clarity
election_data_df = election_data_df.rename(
    columns={"Candidate": "Vote Count",
            "": "Candidate"})
election_data_df.index.names = ["Candidate"]


# Retreive vote totals for each candidate
khan_total = election_data_df.iat[0,0]
correy_total = election_data_df.iat[1,0]
li_total = election_data_df.iat[2,0]
otooley_total = election_data_df.iat[3,0]


# Determine the winner
winner = election_data_df["Vote Count"].idxmax()


# Calculate vote percentages
khan_percentage = float((khan_total / total_votes) * 100)

correy_percentage = float((correy_total / total_votes) * 100)

li_percentage = float((li_total / total_votes) * 100)

otooley_percentage = float((otooley_total / total_votes) * 100)


# Output Voting Analysis to terminal
output = (
        f"\nElection Results\n"
        f"===========================\n"
        f"Total Votes: {total_votes}\n"
        f"===========================\n"
        f"Khan: {khan_percentage:,.3f}% ({khan_total})\n"
        f"Correy: {correy_percentage:,.3f}% ({correy_total})\n"
        f"Li: {li_percentage:,.3f}% ({li_total})\n"
        f"O'Tooley: {otooley_percentage:,.3f}% ({otooley_total})\n"
        f"===========================\n"
        f"Winner: {winner}\n"
        f"===========================\n" 
    )
    
print(output)

    
# Create txt file with voting analysis data
with open(postData, "w") as txt_file:
    txt_file.write(output)
