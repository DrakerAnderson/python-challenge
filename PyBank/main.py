import os
import csv

# INSTRUCTIONS
# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period


# read .csv file with absolute path
csvpath = os.path.join(os.path.abspath('.'), 'PyBank/Resources/budget_data.csv')

with open(csvpath, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')
	header = next(csvreader)

# Variables
total_months = 0
net_total = 0
changes = []
previous_month_profit = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]
date = []

#main loop
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    previous_month_profit = int(next(csvreader)[1])  # get the first profit
    for row in csvreader:
        total_months += 1
        current_profit = int(row[1])
        net_total += current_profit
        changes.append(current_profit - previous_month_profit)
        if current_profit - previous_month_profit > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = current_profit - previous_month_profit
        if current_profit - previous_month_profit < greatest_decrease[1] or greatest_decrease[1] == 0:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = current_profit - previous_month_profit
        previous_month_profit = current_profit

# print analysis results
print("Financial Analysis/n")
print("---------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${sum(changes) / len(changes):.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# write in results.txt
with open('PyBank/analysis/results.txt', 'w') as f:
    f.write("Financial Analysis\n")
    f.write("---------------------\n")
    f.write(f"Total Months: {total_months}\n")
    f.write(f"Total: ${net_total}\n")
    f.write(f"Average Change: ${sum(changes) / len(changes):.2f}\n")
    f.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    f.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")



