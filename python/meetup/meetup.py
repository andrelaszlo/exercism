""" Calculate the date of meetups.
"""

from datetime import date, timedelta
import re

class MeetupDayException(Exception):
    """ Non-existing meetup day. """
    pass

_WEEKDAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
             'sunday']

def days_in_month(year, month):
    """ Iterator that returns each day in a month as a date.
    """
    _day_delta = timedelta(days=1)
    _date = date(year=year, month=month, day=1)
    while _date.month == month:
        yield _date
        _date += _day_delta

def _weekday_number(day):
    """ Convert a weekday's name to an index. Monday = 0, Tuesday = 1, ...
    """
    try:
        return _WEEKDAYS.index(day.lower())
    except ValueError:
        raise MeetupDayException('Unknown weekday: %s' % day)

def _nth_str_to_int(nth_str):
    """ Convert a string like 1st or 13th to an integer.
    """
    match = re.match(r'\d+', nth_str)
    if match:
        return int(match.group())
    raise MeetupDayException('Incorrect format: %s' % nth_str)


def meetup_day(year, month, day, order):
    """ Return a meetup day given a year, month, weekday and an order.
    The order can be 'last', 'teenth' or a count like '1st' or '13th'.
    """
    weekday = _weekday_number(day)

    if order == 'teenth':
        teens = range(13, 20)
        for _date in days_in_month(year, month):
            if _date.weekday() == weekday and _date.day in teens:
                return _date

    if order == 'last':
        last = None
        for _date in days_in_month(year, month):
            if _date.weekday() == weekday:
                last = _date
        return last

    # Otherwise, assume an Nth is given
    nth = _nth_str_to_int(order)
    count = 0
    for _date in days_in_month(year, month):
        if _date.weekday() == weekday:
            count += 1
        if count == nth:
            return _date
    raise MeetupDayException('The %s %s does not exist' % (order, day))
