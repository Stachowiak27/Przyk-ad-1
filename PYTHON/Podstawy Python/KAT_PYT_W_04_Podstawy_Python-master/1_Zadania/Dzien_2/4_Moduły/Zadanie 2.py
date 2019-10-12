
from datetime import date, timedelta

def tomorrow():
    today = date.today()
    print(today)
    day = timedelta(days=1)
    tomorrow = today + day
    return tomorrow

calculate_tomorrow = tomorrow()

print(calculate_tomorrow)