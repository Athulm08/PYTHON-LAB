import time
import datetime

current_datetime = datetime.datetime.now()
print(f"Current date and time: {current_datetime}")

current_year = current_datetime.year
print(f"Current Year: {current_year}")

current_month = current_datetime.month
print(f"Month of the Year: {current_month}")

week_number = current_datetime.isocalendar()[1]
print(f"Week number of the Year: {week_number}")

weekday = current_datetime.weekday()
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(f"Weekday of the Week: {weekdays[weekday]}")

day_of_year = current_datetime.timetuple().tm_yday
print(f"Day of the Year: {day_of_year}")

day_of_month = current_datetime.day
print(f"Day of the Month: {day_of_month}")

day_of_week = current_datetime.strftime('%A')
print(f"Day of the Week: {day_of_week}")

