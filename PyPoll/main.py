import os
import csv


# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote


# read .csv file
# csvpath = os.path.join(os.path.abspath('.'), 'PyPoll/Resources/election_data.csv')

# with open(csvpath, 'r') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter = ',')
#     next(csvreader)
#     rows = list(csvreader)

# # VARIABLES
# total_votes = 0
# candidates= {}
# winner = ""

# # loop through csv rows
# for row in csvreader:
#     total_votes += 1
#     candidate_name = row[2]
# # check for candidate in dictionary and add votes
#     if candidate_name in candidates:
#         candidates[candidate_name] += 1
#     else:
#         candidates[candidate_name] = 1

# # percentage of votes per candidate
# candidate_results = {}
# for candidates, votes in candidates.items():
#     percentage = (votes/total_votes) * 100
#     candidate_results[candidates] = (votes, percentage)

# # find winner
# winner_votes = max(candidates.values())
# winner = [candidate for candidate, votes in candidates.items() if votes == winner_votes][0]
# # winner_votes = max(candidate_results.values())
# for candidate, votes in candidates.items():
#     if votes == winner_votes:
#         winner = candidate

# # print election results
# def print_results(candidate_results, winner):
#     print("Election Results")
#     print("-------------------------")
#     print(f"Total Votes: {sum(votes for votes, _ in candidate_results.values())}")
#     print("-------------------------")
# for candidate, (votes, percentage) in candidate_results.items():
#     print(f"{candidate}: {percentage:.3f}% ({votes})")
#     print("-------------------------")
#     print(f"Winner: {winner}")


csvpath = os.path.join(os.path.abspath('.'), 'PyPoll/Resources/election_data.csv')

# VARIABLES
total_votes = 0
candidate_votes = {}
winner = ""

# read csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    rows = [row for row in csvreader]

# loop through csv rows
for row in rows:
    total_votes += 1
    candidate_name = row[2]
    # check for candidate in dictionary and add votes
    if candidate_name in candidate_votes:
        candidate_votes[candidate_name] += 1
    else:
        candidate_votes[candidate_name] = 1

# percentage of votes per candidate
candidate_results = {}
for candidate, votes in candidate_votes.items():
    percentage = (votes/total_votes) * 100
    candidate_results[candidate] = (votes, percentage)

# find winner
winner_votes = max(candidate_votes.values())
winner = [candidate for candidate, votes in candidate_votes.items() if votes == winner_votes][0]

# Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, (votes, percentage) in candidate_results.items():
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")

# write in results.txt
with open('PyPoll/analysis/results.txt', 'w') as f:
    f.write("Election Results\n")
    f.write("---------------------\n")
    f.write(f"Total votes: {total_votes}\n")
    for candidate, (votes, percentage) in candidate_results.items():
        f.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    f.write("---------------------\n")
    f.write("Winner {winner}")