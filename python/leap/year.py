def is_leap_year(n):
    """Check if a year is a leap year or not."""
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False
