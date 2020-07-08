# You are given the following information, but you may prefer to do some research for yourself.
# 
# - 1 Jan 1900 was a Monday.
# - Thirty days has September,
# - April, June and November.
# - All the rest have thirty-one,
# - Saving February alone,
# - Which has twenty-eight, rain or shine.
# - And on leap years, twenty-nine.
# - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# First thing that came to my mind was to make use {lubridate} functions to filter the first of the month (`day`) and 
# days on Sunday (`wkday`) from a vector of all possible dates in the 20th century.

library(lubridate)
# ymd("2000-12-31")-ymd("1901-01-01")
# Time difference of 36524 days

# --- Vector with every date within the 20th century
# --- Perhaps a "better" way to do this would be to add one month up until 1/1/2001
dates <- ymd("1901-01-01") + 0:36524

length(dates[day(dates) == 1 & wday(dates) == 1])
# [1] 171
