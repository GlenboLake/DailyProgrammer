import datetime

while True:
    try:
        [year, month, date] = list(map(int, input().split()))
    except:
        break

    then = datetime.date(year, month, date)
    today = datetime.date.today()
    days = (then - today).days

    print('{} days from {} to {}'.format(days, today, then))
