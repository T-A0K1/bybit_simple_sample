import datetime as dt

def fromUNIXmStoDatetime(UNIXmSecond):
    return dt.datetime.fromtimestamp(UNIXmSecond/1000)
