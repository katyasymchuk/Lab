import datetime
import sys
from random import randint

def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform


def home_work_numbers(is_even):
    start_number = 1 if not is_even else 0
    return range(start_number, 100, 2)


def func_with_possible_error():
    return randint(0, 1)