import os
import datetime
from absconbest_payroll.spreadsheetManipulation import *
from absconbest_payroll.visualization import *
from absconbest_payroll.reportGeneration import *

#Convert the data type of today to make it readable
date_today=datetime.date.today().strftime('%b %d, %Y')

#Assign the 'absconbest_payroll.xlsx' file's location
xlsx_location=os.path.expanduser("~/Desktop/absconbest_payroll/absconbest_payroll.xlsx")

#Read activities and their time in hour
data=read_xlsx(xlsx_location, 'A, C', 30)
data=get_sorted(data, 'TIH')

#Read works and their time in hour
data2=read_xlsx(xlsx_location, 'G, I', 30)
data2=get_sorted(data2, 'TIH')

#Plot and print the data's graph
visualize(
    data,
    data2,
    date_today,
    'Activity',
    'TIH',
    'Work',
    'TIH',
)

#Generate a report
#Read the calculated wage, rate per hour, time in hours, and the type of work
payroll=read_xlsx(xlsx_location, "G, H, I, L, K", 33)
payroll=get_sorted(payroll, "Wage")
#Read the profile including the name, email, and title
title=read_xlsx(xlsx_location, "N", 30)
generate_report(
    date_today, title['Profile'][0], title['Profile'][1],
    title['Profile'][2], payroll
)

