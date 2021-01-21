# Import needed modules
import csv
import os

# Files to load and output (Remember to change these)
file_input = os.path.join("Resources", "budget_data.csv")
file_output = os.path.join("Analysis", "budget_analysis.txt")

# Initilizing counters and variables
tot_months = 0
month_change = []
net_list_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
tot_net = 0

# Importing the csv file
with open(file_input, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    first_row = next(csvreader)
    tot_months = tot_months + 1
    tot_net = tot_net + int(first_row[1])
    prev_net = int(first_row[1])

    for row in csvreader:
        tot_months = tot_months + 1
        tot_net = tot_net + int(row[1])
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_list_change = net_list_change + [net_change]
        month_change = month_change + [row[0]]

        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Calculate the Average Net Change
net_monthly_avg = sum(net_list_change) / len(net_list_change)

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {tot_months}\n"
    f"Total: ${tot_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print output to terminal
print(output)

# Export the results to text file
with open(file_output, "w") as txt_file:
    txt_file.write(output)