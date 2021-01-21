# Import needed modules
import csv
import os

# Files to load and output (Remember to change these)
file_input = os.path.join("Resources", "election_data.csv")
file_output = os.path.join("Analysis", "election_analysis.txt")

# Initilizing counters and variables
tot_votes = 0
cand_option = []
cand_votes = {}
winner_cand = ""
winner_count = 0

# Importing the csv 
with open(file_input) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    for row in reader:
        print(". ", end=""),
        tot_votes = tot_votes + 1
        cand_name = row[2]
        if cand_name not in cand_option:
            cand_option.append(cand_name)
            cand_votes[cand_name] = 0
        cand_votes[cand_name] = cand_votes[cand_name] + 1

# Print the final vote count and export text file
with open(file_output, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {tot_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

    # Determine the winner by looping through the counts
    for candidate in cand_votes:
        votes = cand_votes.get(candidate)
        vote_percentage = float(votes) / float(tot_votes) * 100
        if (votes > winner_count):
            winner_count = votes
            winner_cand = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate 
    winner_cand_summary = (
        f"-------------------------\n"
        f"Winner: {winner_cand}\n"
        f"-------------------------\n")
    print(winner_cand_summary)

    # Export winning candidate's name to the text file
    txt_file.write(winner_cand_summary)
