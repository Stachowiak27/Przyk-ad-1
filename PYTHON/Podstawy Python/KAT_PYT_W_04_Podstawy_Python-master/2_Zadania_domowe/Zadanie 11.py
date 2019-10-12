import datetime

def format_date(day,month,year):
    months_pl = ["stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca",
                 "lipca", "sierpnia", "września", "października", "listopada", "grudnia"]

    if month > 12:
        return None
    if month == 2 and day > 28:
        return None
    if month in(1,3,5,7,8,10,12) and day>31:
        return None
    if month in(4,6,9,11) and day > 30:
        return None
    else:

        return "{} {} {}r.".format(day,months_pl[month-1],year)


d = format_date(27, 12, 2016)
print(d)
d = format_date(12,13, 2016)
print(d)