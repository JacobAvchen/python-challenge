import os
import csv

HighChange = 0
LowChange = 0
NetProfit = 0
length = 0
ChangeLog = []


dir_path = os.path.dirname(os.path.realpath(__file__))
csvpath = os.path.join(dir_path, '..', 'Resources', '03-Python_homework_assignment_PyBank_Resources_budget_data.csv')
output_path = os.path.join(dir_path, '..', 'output', 'bankOutput.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        length +=1
        NetProfit += int(row[1])

        if length > 1:
            ChangeLog.append((int(row[1]) - prevRow))
            if ((int(row[1])) - prevRow) > HighChange:
                HighChange = ((int(row[1])) - prevRow)
                HighChangeMonth = row[0]
            elif ((int(row[1])) - prevRow) < LowChange:
                LowChange = ((int(row[1])) - prevRow)
                LowChangeMonth = row[0]
        
        prevRow = int(row[1])

AverageChange = round((sum(ChangeLog) / len(ChangeLog)), 2)

print("Financial Analysis")
print("-------------------------------------")
print("Total Months: " + str(length))
print("Total: $" + str(NetProfit))
print("Average Change: $" + str(AverageChange))
print("Greatest Increase in Profits: " + HighChangeMonth + ", $" + str(HighChange))
print("Greatest Decrease in Profits: " + LowChangeMonth + ", $" + str(LowChange))

with open(output_path, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["Total Months", length])
    csvwriter.writerow(["Total", NetProfit])
    csvwriter.writerow(["Average Change", AverageChange])
    csvwriter.writerow(["Greatest Increase in Profits", HighChangeMonth, HighChange])
    csvwriter.writerow(["Greatest Decrease in Profits", LowChangeMonth, LowChange])



        