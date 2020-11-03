""" read and open csv file """
import csv
import sys
from analyze import simple_moving_average, simple_moving_average_days, exponential_moving_average

SPREADSHEET = 'HistoricalData.csv'

def read_data(data, item):
    """ create dict reader and import analyze functions"""
    #read csv as dict reader
    read = csv.DictReader(data)
    try:
        # simple_moving_average(read, item)
        # simple_moving_average_days(read, item, 20)
        exponential_moving_average(read, item, 12)
    # exit from python
    except csv.Error as _e:
        sys.exit('file {}, line {}: {}'.format(data, read.line_num, _e))


def main(column):
    """ open csv file """
    with open(SPREADSHEET) as csvfile:
        return read_data(csvfile, column)

main('Close')
