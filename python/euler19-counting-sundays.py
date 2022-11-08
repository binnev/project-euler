# -*- coding: utf-8 -*-
"""
Counting Sundays
Problem 19
You are given the following information, but you may prefer to do some research
for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?

"""
# calculate the number of DAYS from 1 jan 1900 to 31 dec 2000
# then you can calculate the number of sundays
from python.tools.utils import profile

years = {}
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def leap_year(year):
    leap = False  # assume false
    if year % 4 == 0:  # if year is evenly divisible by 4
        if year % 100 == 0:  # if year is a century
            if year % 400 == 0:  # AND evenly divisible by 400
                leap = True
        else:  # if year not a century but still evenly divisible by 4
            leap = True
    return leap


def calc_weekday(start_weekday, days_elapsed):
    return start_weekday + days_elapsed % 7


def count_weekdays(start_weekday, days_elapsed, weekday):
    weeks, remainder = divmod(days_elapsed, 7)
    add = 1 if weekday in range(start_weekday, start_weekday + remainder) else 0
    return weeks + add


@profile
def euler19():
    """this was ugly, but I misinterpreted the problem at first, and made several
    stupid typos..."""

    # calculate the days in each year from 1900 to 2000
    years = {y: 366 if leap_year(y) is True else 365 for y in range(1900, 2000 + 1)}

    # extract the total number of days from 1 jan 1901 to 31 dec 2000
    days_elapsed = sum(years[y] for y in range(1901, 2000 + 1))

    # find out the weekday of 1 jan 1901
    start = calc_weekday(
        0, years[1900]  # 1 jan 1900 was a monday  # the number of days in 1900
    )  # the next day will be 1 jan 1901

    sundays = count_weekdays(start, days_elapsed, 6)

    start1900 = 0  # 1 jan 1900 = monday
    months = ("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec")

    sundays = []
    weekday = start1900
    # need to start the years from the known monday at the start of 1900
    # but we need to start counting sundays from 1901.
    for year in range(1900, 2000 + 1):
        for month in months:
            # calculate days in current month
            if month in ("sep", "apr", "jun", "nov"):
                month_days = 30
            elif month == "feb":
                month_days = 29 if leap_year(year) else 28
            else:
                month_days = 31

            e = "leap year!" if leap_year(year) else ""
            for monthday in range(1, month_days + 1):
                # increment sundays if sunday
                c = ""
                if weekday == 6 and year >= 1901 and monthday == 1:
                    sundays.append("{} {} {}".format(year, month, monthday))
                    #                time.sleep(0.5)
                    c = "magic sunday!"

                #            print("considering",year,month,monthday,weekdays[weekday],e,c)

                monthday += 1  # increment day
                weekday += 1  # increment weekday too
                weekday = weekday % 7  # keep in range 0..6

    return len(sundays)


if __name__ == "__main__":
    assert euler19() == 171
