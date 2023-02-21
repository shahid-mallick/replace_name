# import calendar
# year =int(input("Enter the Year :"))
# mon = int(input("Enter the Month :"))
# print(calendar.month(year, mon))

from datetime import date

# Driver program
date1 = date(2018, 12, 13)
date2 = date(2019, 2, 25)
days = (date2-date1).days

print(days, "days")
