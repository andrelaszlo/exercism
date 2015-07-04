from datetime import timedelta

_gigasecond_delta = timedelta(seconds=10**9)

def add_gigasecond(date):
    return date + _gigasecond_delta
