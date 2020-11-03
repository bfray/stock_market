from fractions import Fraction

""" analyze data functions for market py """

data = {}

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
    smooth = Fraction(smoothing, (1 + days))
    if smooth:
        return float(smooth)
    return 0


def exponential_moving_average(read, item, days):
    """ exponential moving average """
    rows = list(read)
    for i, row in enumerate(rows):
        close = float(row['Close'])
        ema = None
        smoothing = 2
        if i <= days:
            if i == 0:
                ema = close
            else:
                ema = (close * smoothing_days(smoothing, i)) + data[i-1] * (1 - smoothing_days(smoothing, i))
            data[i] = ema
    print data
    return data
