from datetime import datetime
from utils.constants import DATE_FORMAT

def format_date(date_str):
    """
    Convert a date string to a formatted date object.
    """
    return datetime.strptime(date_str, DATE_FORMAT)

def current_date_str():
    """
    Get the current date as a string in the specified format.
    """
    return datetime.now().strftime(DATE_FORMAT)
