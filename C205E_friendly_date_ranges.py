'''
http://www.reddit.com/r/dailyprogrammer/comments/2ygsxs/20150309_challenge_205_easy_friendly_date_ranges/

The goal of this challenge is to implement a way of converting two dates into a
more friendly date range that could be presented to a user. It must not show
any redundant information in the date range. For example, if the year and month
are the same in the start and end dates, then only the day range should be
displayed. Secondly, if the starting year is the current year, and the ending
year can be inferred by the reader, the year should be omitted also.
'''
from datetime import datetime
import re


# Taken from codegolf
ordinal = lambda n: "%d%s" % (n, "tsnrhtdd"[(n / 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])

def readable(datesString):
    dates = datesString.split(' ')
    fmat = '%Y-%m-%d'
    before = datetime.strptime(dates[0], fmat)
    after = datetime.strptime(dates[1], fmat)
    current_year = datetime.now().year
    # Five optional fields: Year for the first date, hyphen between dates, and M/D/Y for the second date.
    display = [True] * 5
    # If they're the same date, just display one
    if before == after:
        display[1:] = [False] * 4
    elif before.year == after.year:
        # If they're in the same year, just display it at the end
        display[0] = False
        if before.month == after.month:
            display[2] = False
        if before.year == current_year:
            # But this year doesn't need anything displayed
            display[4] = False
    elif before.year == current_year and (after - before).days < 365:
        # If the date range starts this year, and ends less than a year from now, no need to display the first year
        display[0] = display[4] = False
    
    rv = "{} {}{} {} {} {}{}".format(
                                   before.strftime("%B"),
                                   ordinal(before.day),
                                   ', ' + str(before.year) if display[0] else '',
                                   '-' if display[1] else '',
                                   after.strftime("%B") if display[2] else '',
                                   ordinal(after.day) if display[3] else '',
                                   ', ' + str(after.year) if display[4] else ''
                                   )
    return re.sub(' +', ' ', rv).strip()

print(readable('2015-07-01 2015-07-04'))
print(readable('2015-12-01 2016-02-03'))
print(readable('2015-12-01 2017-02-03'))
print(readable('2016-03-01 2016-05-05'))
print(readable('2017-01-01 2017-01-01'))
print(readable('2022-09-05 2023-09-04'))