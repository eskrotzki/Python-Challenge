import os
import csv

polls_csv = os.path.join("Resources", "election_data.csv")

count=0
candidate = []
unique = []
vote_count = []
vote_percent = []

with open(polls_csv, newline = "") as csvfile:
    csvreader=csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)


    for row in csvreader: 
        count = count + 1
        candidate.append(row[2])

    for i in candidate:
        unique.append(i)
        j = candidate.count(i)
        vote_count.append(j)

        percent= (j/count)*100
        vote_percent.append(percent)

    winning_vote = max(vote_count)
    winner = unique[vote_count.index(winning_vote)]


print(f"Election Results")

print("              ")

print(f"Total Votes: {count}")

print("              ")

for x in range(len(unique)):
    print(f"{unique[x]} : {vote_percent[x]}% ({vote_count[x]})")

print(f"Winner: {winner}")


with open("PyPoll.txt", "w") as text:
    
    text.write(f"Election Results")

    text.write("              ")

    text.write(f"Total Votes: {count}")

    text.write("              ")

    for x in range(len(unique)):
        text.write(f"{unique[x]} : {vote_percent[x]}% ({vote_count[x]})")

    text.write(f"Winner: {winner}")