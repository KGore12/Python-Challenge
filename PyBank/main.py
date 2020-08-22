import os
import csv


# All variables and totals
total_months = 0
net_PandL = 0
month_total = []
avg_change = []

greatest_increase = 0
greatest_decrease = 0
greatest_In_month = 0
greatest_De_month = 0


# Get Budget.csv from the Pybank Resources folder 
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

# Open PyBank Budget.csv file 
with open(csvpath, 'r') as csvfile:
    
    # Use delimiter to separate data ","
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Instruct to read head row
    csv_header = next(csvreader)
    row = next(csvreader)
    
    # Collect data for the PandL calculations & also set any variables for rows -total Number Of Months, Net Amount Of 
    previous_row = int(row[1])
    total_months += 1
    net_PandL += int(row[1])
    greatest_increase = int(row[1])
    greatest_In_month = row[0]
    
    # for every row of data after header
    for row in csvreader:
        
        # Use calculation for total # of months in all datasets 
        total_months += 1
        
        # Use calculation for net_amount of PandL for entire period
        net_PandL += int(row[1])

        # Show calculations changes from the current month to previous months
        revenue_change = int(row[1]) - previous_row
        avg_change.append(revenue_change)
        previous_row = int(row[1])
        month_total.append(row[0])
        
        # Calculate your greatest increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_Inmonth = row[0]
            
        # Calculate your greatest decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_Demonth = row[0]  
        
    # What is the average change and what is the date?
    avg_change = sum(avg_change)/ len(avg_change)
    
    highest = max(avg_change)
    lowest = min(avg_change)


#Print breakdown Analysis
print(f"Financial Analysis")
print(f"----_-------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_Inmonth}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_Demonth}, (${lowest})")

#File To Write To - specification
output_file = os.path.join('..', 'PyBank', 'Resources', 'budget_data_outcome.text')

#Variables - Opening the File in "Write" Mode
with open(output_file, 'w') as txtfile:

#New Data
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_amount}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")


