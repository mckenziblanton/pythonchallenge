import os 
import csv

#current location > raw_data > file you need 
csvpath = os.path.join('.',"raw_data", "budget_data_1.csv")

# read csv file 
with open(csvpath, newline='') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    months = 0
    total_revenue = 0 
    x = 0 

    revenue = []
    dates = []
    change_list = [] 

    for row in csvreader: 
        if str(row[0]) != "Date":
            months = months + 1
            dates.append(row[0])
        if str(row[1]) != "Revenue":
            total_revenue = total_revenue + int(row[1])
            revenue.append(int(row[1]))
    print("Financial Analysis")
    print("------------------")
    print("Total Months: " + str(months))
    print("Total Revenue: " + str(total_revenue))
    
    for i in range(len(revenue)-1):
        change_list.append(revenue[x+1] - revenue[x]) 
        x = x + 1

    #greatest decrease in revenue
    decrease= min(change_list)
    #print(decrease)
    #greatest increase in revenue 
    increase= max(change_list)
    #print(increase)

    x = 0
    for i in range(len(revenue)-1):
        if decrease == revenue[x+1] - revenue[x]:
            decrease_date = dates[x+1]
        x = x + 1
    #print(decrease_date)
    x = 0
    for i in range(len(revenue)-1):
        if increase == revenue[x+1] - revenue[x]:
            increase_date = dates[x+1]
        x = x + 1
    #print(increase_date)
        
    #average change between months
    average = sum(change_list)/len(change_list)
    print("Average Revenue Change: " + str(average))
    print("Greatest Increase in Revenue: " + increase_date + "($" + str(increase) + ")")
    print("Greatest Decrease in Revenue: " + increase_date + "($" + str(decrease) + ")")

