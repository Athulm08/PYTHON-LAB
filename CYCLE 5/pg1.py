import calendar

def check_leap_year(year):
    if calendar.isleap(year):
        return f"{year} is a leap year."
    else:
        return f"{year} is not a leap year."

year = int(input("Enter a year: "))

print(check_leap_year(year))
