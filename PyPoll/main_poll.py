import os
import csv

voteCount = 0
KhanCount = 0
LiCount = 0
CorreyCount = 0
OTooleyCount = 0

dir_path = os.path.dirname(os.path.realpath(__file__))
csvpath = os.path.join(dir_path, '..', 'Resources', '03-Python_homework_assignment_PyPoll_Resources_election_data.csv')
output_path = os.path.join(dir_path, '..', 'output', 'pollOutput.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        voteCount += 1

        if row[2] == "Khan":
            KhanCount += 1
        elif row[2] == "Li":
            LiCount += 1
        elif row[2] == "Correy":
            CorreyCount += 1
        elif row[2] == "O'Tooley":
            OTooleyCount += 1

KhanPerc = round(((KhanCount / voteCount) * 100), 2)
LiPerc = round(((LiCount / voteCount) * 100), 2)
CorreyPerc = round(((CorreyCount / voteCount) * 100), 2)
OTooleyPerc = round(((OTooleyCount / voteCount) * 100), 2)

if ((KhanCount > LiCount) & (KhanCount > CorreyCount) & (KhanCount > OTooleyCount)):
    winner = "Khan"
elif ((LiCount > KhanCount) & (LiCount > CorreyCount) & (LiCount > OTooleyCount)):
    winner = "Li"
elif ((CorreyCount > KhanCount) & (CorreyCount > LiCount) & (CorreyCount > OTooleyCount)):
    winner = "Correy"
elif ((OTooleyCount > KhanCount) & (OTooleyCount > LiCount) & (OTooleyCount > CorreyCount)):
    winner = "O'Tooley"
else:
    winner = "John Cena idk"

print("Election Results")
print("---------------------------------")
print(f"Total Votes: {voteCount}")
print("---------------------------------")
print(f"Khan: {KhanPerc}% ({KhanCount})")
print(f"Correy: {CorreyPerc}% ({CorreyCount})")
print(f"Li: {LiPerc}% ({LiCount})")
print(f"O'Tooley: {OTooleyPerc}% ({OTooleyCount})")
print("---------------------------------")
print(f"The winner is {winner}!")
print("---------------------------------")


with open(output_path, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Election Results", "Percentage Won", "Total Votes Won"])
    csvwriter.writerow(["Total Votes", voteCount])
    csvwriter.writerow(["Khan", KhanPerc, KhanCount])
    csvwriter.writerow(["Correy", CorreyPerc, CorreyCount])
    csvwriter.writerow(["Li", LiPerc, LiCount])
    csvwriter.writerow(["O'Tooley", OTooleyPerc, OTooleyCount])
    csvwriter.writerow(["Winner", winner])