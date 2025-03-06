#!/usr/bin/env python3
from os import mkdir

# Let's initiate the years interval: 

year_start = 1992
year_end = 2092

# Also the months: January...December (01...12) 
# ... and days: (01-31)

month_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Let's create directories as the calendar days: MKDIR 
# The format of every directory tree: YYYY/YYYY-MM_Month/YYYY-MM-DD
# Additionally, text Markdown documents (.md) will be created for each day 

for years in range(year_start, (year_end+1)):
    year = str(years)
    mkdir(year)    
    for months in range(1, (len(month_name)+1)):
        if (months < 10):
            month = "0" + str(months)
            mkdir(year + "/" + year + "-" + month + "_" + month_name[months-1])
        else:
            month = str(months)
            mkdir(year + "/" + year + "-" + month + "_" + month_name[months-1])
        if months == 4 or  months == 6 or months == 9 or months == 11:
            days_range = 30
        elif years%4 == 0 and months == 2:
            days_range = 29
        elif years%4 != 0 and months == 2:
            days_range = 28
        else:
            days_range = 31
        for days in range(1, (days_range+1)):
            if (days < 10):
                day = "0" + str(days)
                mkdir(year + "/" + year + "-" + month + "_" + month_name[months-1] + "/" + year + "-" + month + "-" + day)
                file_name = year + "/" + year + "-" + month + "_" + month_name[months-1] + "/" + year + "-" + month + "-" + day + "_.md"
                f = open(file_name, "w")
                f.write("# Note is empty...")
                f.close()
            else:
                day = str(days)
                mkdir(year + "/" + year + "-" + month + "_" + month_name[months-1] + "/" + year + "-" + month + "-" + day)
                file_name = year + "/" + year + "-" + month + "_" + month_name[months-1] + "/" + year + "-" + month + "-" + day + "_.md"
                f = open(file_name, "w")
                f.write("# Note is empty...")
                f.close()

"""
This code was written independently without using ChatGPT or another AI tool!
Purpose of writing code: self-practice and personal usage.
Author: Vitaly A.
Contact: https://vitaly92a.github.io
"""
