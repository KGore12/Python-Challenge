import os
import csv


# All the variables and totals for assignment
total_months = 0
net__total_profits_losses = 0
average_changes_profits_losses = []
greatest_increase_profits = 0
greatest_decrease_losses = 0
greatest_increase_month = 0
greatest_decrease_month = 0


# Get Budget.csv from the Pybank Resources folder 
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

# Open PyBank Budget.csv file 
with open(csvpath, 'r') as csvfile:
    
    # Use delimiter to separate data by comma ","
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Instructions to read head row
    csv_header = next(csvreader)
    row = next(csvreader)
    
    # Collect data for the Profits and Losses calculations & 
        # also set any variables for rows -total Number Of Months, Net Amount Of 

    previous_row = int(row[1])

    
    # for every row of data after header
    for row in csvreader:

        # Use calculation for total # of months in all datasets 
        total_months += 1
        
        # Use calculation for net_amount of PandL for entire period
        net__total_profits_losses += int(row[1])

        # Show calculations changes from the current month to previous months
                #check if error is thrown for total_months.append  it was month_total & you removed that variable above
        revenue_change = int(row[1]) - previous_row
        average_changes_profits_losses.append(revenue_change)
        previous_row = int(row[1])

        
        # Calculate your greatest increase for the profits and which month
        if int(row[1]) > greatest_increase_profits:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        # Calculate your greatest decrease
        if int(row[1]) < greatest_decrease_losses:
            greatest_decrease_losses = int(row[1])
            greatest_decrease_month = row[0]  
        
    # What is the average change and what is the date?
    average_changes = sum(average_changes_profits_losses)/ len(average_changes_profits_losses)
    
    highest = max(average_changes_profits_losses)
    lowest = min(average_changes_profits_losses)



#Print breakdown Analysis
print(f"Financial Analysis")
print(f"----_-------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net__total_profits_losses}")
print(f"Average Change: ${average_changes:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")


#File To Write To - specification
output_file = os.path.join('..', 'PyBank', 'Resources', 'budget_data_outcome.text')

#Variables - Opening the File in "Write" Mode
with open(output_file, 'w') as txtfile:

#New Data
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net__total_profits_losses}\n")
    txtfile.write(f"Average Change: ${average_changes}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")


