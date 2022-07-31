# Завдання 2
from vacations_calendar import calendar


def check(date_str: str):
    try:
        if len(date_str.split('/')) != 3 or len(date_str.split('/')[0]) != 2 or len(date_str.split('/')[1]) != 2:
            print('Wrong date format, must be DD/MM/YYYY')
            return None
        if date_str[:5] in calendar.keys():
            return calendar[date_str[:5]]
        else:
            return None
    except:
        print('Wrong date format, must be DD/MM/YYYY')
        return None

