import datetime


def unixToDateTime(unixTime):
    return datetime.datetime.fromtimestamp(unixTime).strftime('%Y-%m-%d %H:%M:%S')
