#Gary Li
#10/2/17
#fri13.py
from calendar import weekday
from datetime import date
day = date.today().day
month = date.today().month
year = date.today().year
print(month, day, year)
friday13 = 0
if day>13 and month!=12:
    month=month+1
else:
    month==1
    year= year+1
if friday13<=10:
    weekday = weekday(year,mont,13)
    if weekday ==5:
        friday13 = friday13+1
        print(month, '13', year)
        if month!=12:
            month+ month+1
        else month == 1
        year = year + 1
    else:
        if month!=12:
            month= month +1
        else:
            month == 1
            year = year + 1
print(weekday(year, month, day))