# задание 1
import datetime
from datetime import timezone

def my_functiom(year, month, day):
    input_date = datetime.date(year, month, day)
    nomer = input_date.isocalendar()[1]
    return nomer
year = 2015
month = 6
day = 16
nomer = my_functiom(year, month, day)
print(nomer)

# задание 3

# def sunday(year):
#     d = datetime.date(year, 1, 1)                    
#     d += datetime.timedelta(days=(6 - d.weekday()))   
#     while d.year == year:                           
#         yield d                                      
#         d += datetime.timedelta(days=7)              
# for i in sunday(year):
#     print(i)

# задание 4

def addYears(date, years):
    try:
        return date.replace(year=date.year + years)
    except ValueError:
        if date.month == 2 and date.day == 29:
            return date.replace(year=date.year + years, day=28)

print(addYears(datetime.date(2015, 1, 1), -1))
print(addYears(datetime.date(2015, 1, 1), 0))
print(addYears(datetime.date(2015, 1, 1), 2))
print(addYears(datetime.date(2000, 2, 29), 1))


# задание 1

grinvich = datetime.now(timezone.utc)
print(f"по гринвичу: {grinvich.strftime('%Y-%m-%d %H:%M:%S')}")

mestnoe = datetime.now()
print(f"местное: {mestnoe.strftime('%Y-%m-%d %H:%M:%S')}")

# задание 2

def raznica(date1, date2):
    date_format = "%Y-%m-%d"
    datetime1 = datetime.strptime(date1, date_format)
    datetime2 = datetime.strptime(date2, date_format)
    return abs((datetime2 - datetime1).days)

date1 = input("введите дату в виде ГГГГ-ММ-ДД: ")
date2 = input("введите вторую дату в виде ГГГГ-ММ-ДД: ")

print(raznica(date1, date2))

# задание 3

