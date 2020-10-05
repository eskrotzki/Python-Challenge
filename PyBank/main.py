import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

# Need to create to analyze Total months
# Net total amount of "profit/losses" over entire period
# Average of changes in P/L over entire period 
# Greates increase and decrease (Date and Amount) over entire period

months = []
revenue = []
month_change=[]
revenue_change=[]

with open(budget_csv, newline = "") as csvfile:
    csvreader= csv.reader(csvfile, delimiter = ",")
    print(csvreader)
    next(csvreader)


    for row in csvreader:
        months.append(row[0])
        revenue.append(row[0])
    print(len(months)
    rev = map(int, revenue)
    total_rev = sum(rev)


    i=0
    for i in range(len(revenue)-1):
        loss = int(revenure[i+1]) - int(revenue[i])
        revenue_change.append(loss)
    total = sum(revenue_change)

    month_change= total/len(revenue_change)
    print(month_change)

    profit_inc = max(revenue_change)
    print(profit_inc)
    j = revenue_change.index(profit)
    month_inc = months[j+1]

    profit_dec = max(revenue_change)
    print(profit_dec)
    e = revenue_change.index(profit_dec)
    month_dec = months[e+i]


    print("Financial Analysis")

    print("                   ")

    print(f"Total Months: {months}")
    print(f"Total: {revenue}")
    print(f"Average Change {month_change}")
    print(f"Greatest increase in profits: {month_inc} {profit_inc}")
    print(f"Greatest increase in profits: {month_dec} {profit_dec}")

with open("PyBank.txt", "w") as text:
    
    text.write("Financial Analysis")

    text.write("                   ")

    text.write(f"Total Months: {months}")
    text.write(f"Total: {revenue}")
    text.write(f"Average Change {month_change}")
    text.write(f"Greatest increase in profits: {month_inc} {profit_inc}")
    text.write(f"Greatest increase in profits: {month_dec} {profit_dec}")
    