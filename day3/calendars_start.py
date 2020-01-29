#
# Example file for working with Calendars
#

# import the calendar module
import calendar

# create a plain text calendar
# cal = calendar.TextCalendar(calendar.MONDAY)
# st = cal.formatmonth(2020, 1, 0, 0)
# print(st)

# create an HTML formatted calendar
cal_html = calendar.HTMLCalendar(calendar.SUNDAY)
st = cal_html.formatmonth(2020, 1)
print(st)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
# for day in cal.itermonthdates(2020, 1):
#     if day.year == 2020 and day.month == 1:
        # print(day)

# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms


# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
