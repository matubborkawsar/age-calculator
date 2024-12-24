import datetime

currentYear = datetime.datetime.now().year
currentMonth = datetime.datetime.now().month
currentDay = datetime.datetime.now().day

birthDay = int(input("Enter your birth day : "))
birthMonth = int(input("Enter your birth month : "))
birthYear = int(input("Enter your birth year : "))

def calculateAge():
    years = currentYear - birthYear
    months = currentMonth - birthMonth
    days = currentDay - birthDay
    print(years, "Years" , months, "Months", days, "Days")

if birthDay > currentDay:
    currentDay += 30
    birthMonth += 1
    if birthMonth > currentMonth:
        currentMonth += 12
        birthYear += 1
        calculateAge()
    else:
        calculateAge()
else:
    if birthMonth > currentMonth:
        currentMonth += 12
        birthYear += 1
        calculateAge()
    else:
        calculateAge()