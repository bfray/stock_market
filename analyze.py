""" analyze data functions for market py """

def simple_moving_average(read, item):
    """ calculate the simple moving average total data"""
    rows = list(read)
    totalrows = len(rows)
    if totalrows:
        total = sum(float(r[item]) for r in rows)
        print total / totalrows
        return total / totalrows
    return 0

def simple_moving_average_days(read, item, days):
    """ calculate the simple moving average for number of days"""
    rows = list(read)
    for i, row in enumerate(rows):
        if i == days:
            result = sum(float(row[item]) for x in range(0, i) if x < i) / days
            print result
            return result
    return 0

def smoothing_days(smoothing, days):
    """ ema multiplier """
    smooth = smoothing / (1 + days)
    if smooth:
        return smooth
    return 0

def exponential_moving_average(read, item):
    """ exponential moving average """
    rows = list(read)
    lastrow = rows[-1][item]
    secondlastow = rows[-2][item]
    smoothing = 2
    ema_yesterday = (float(lastrow) * (1 - (smoothing_days(smoothing, 1))))
    ema_today = (float(secondlastow) * smoothing_days(smoothing, 1))
    ema = ema_today + ema_yesterday
    print ema
    return ema
