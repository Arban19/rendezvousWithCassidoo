from datetime import datetime

def days_between(date_0, date_1):
    format = "%b %d, %Y"

    try:
        dte_0 = datetime.strptime(date_0, format)
        dte_1 = datetime.strptime(date_1, format)
    except ValueError:
        return None

    diff = dte_1 - dte_0

    return diff.days

assert days_between('Jan 1, 2024', 'Jan 29, 2024') == 28
assert days_between('Feb 29, 2020', 'Oct 31, 2023') == 1340
assert days_between('Feb 29, 2020', 'Mar 32, 2023') == None
assert days_between('Today', 'Tomorrow') == None
