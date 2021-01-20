import os
import csv
os.chdir("D:/UTSA/python-challenge/PyBank")
print("Directory changed")
#Read the CSV file 
file="Resources/budget_data.csv"
with open(file,"r")as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header=next(csvreader)
    months=0
    pro_loss=0
    value_past=0
    value=0
    change=0
    change_sum=0
    g_inc_change=0
    g_dec_change=0
    change_mem=0
    for row in csvreader:
        #Total number of months
        months= months+1
        #net total amount of "profit and losses"
        pro_loss=pro_loss+int(row[1])
        #Average of the changes in profit and losses
        if value_past == 0:
            value_past=float(row[1])
        else:
            value=float(row[1])
            change=value-value_past
            #Save the output variables of greatest and lowes change
            if change>g_inc_change:
                g_inc_month= row[0]
                g_inc_change= change
            elif change<g_dec_change:
                g_dec_month=row[0]
                g_dec_change=change
            change_sum=change_sum+change
            value_past=float(row[1])
    #Change average calculation
    change_avg=change_sum/(months-1)
    #Output code
    output=f"""
    Finantial Analysis
    --------------------
    Total Months : {months}
    Total : ${pro_loss}
    Average Change: {change_avg:.2f}
    Greatest Increase in Profits : {g_inc_month} (${g_inc_change})
    Gratest Decrease in Profits : {g_dec_month} (${g_dec_change})

    ----------------------
    """
    output_txt="Analysis/Analysis.txt"
    with open(output_txt,"w")as file:
        file.write(output)
    print(output)