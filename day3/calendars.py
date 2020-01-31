#
# Example file for working with Calendars
#

# import the calendar module
import calendar
from datetime import datetime


# create a plain text calendar
def plain_text_calendar():
    cal = calendar.TextCalendar(calendar.MONDAY)
    st = cal.formatmonth(2020, 1, 0, 0)
    print(st)


# create an HTML formatted calendar
# cal_html = calendar.HTMLCalendar(calendar.SUNDAY)
# st = cal_html.formatmonth(2020, 1)
# print(st)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
# for day in cal.itermonthdates(2020, 1):
#     if day.year == 2020 and day.month == 1:
# print(day)

# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
# for name in calendar.month_name:
#         print(name)

# for name in calendar.day_name:
#         print(name)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
cal = calendar.Calendar(firstweekday=0)  # Create a calendar
months = calendar.month_name[1:]  # Get the names of calendar months
today = datetime.today()
meeting_days = []  # Store days of month for team meeting
year = {}

for month in range(0, 12):
    for day in cal.itermonthdates(2020, month):
        month = months[day.month - 1]
        # If day is on Friday, add to meeting days
        if day.isoweekday() == 5:
            meeting_days.append(day.day)
            if month in year:
                year[month].append(day.day)
            else:
                year[month] = [day.day]

for x, month_number in zip(months, year.keys()):
    print(f"The month name is {x}, and the month number is {month_number}")

print(year)
print(meeting_days)
