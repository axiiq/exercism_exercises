from datetime import date, datetime, timedelta

def add(moment):
    gigasecond = timedelta(seconds=1_000_000_000) 
    return moment + gigasecond
