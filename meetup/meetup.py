import calendar
from datetime import date


def meetup_day(year, month, day_name, order):
    def _week_days_in_month():
        month_cal = calendar.monthcalendar(year, month)
        day = {
            'Monday':    calendar.MONDAY,
            'Tuesday':   calendar.TUESDAY,
            'Wednesday': calendar.WEDNESDAY,
            'Thursday':  calendar.THURSDAY,
            'Friday':    calendar.FRIDAY,
            'Saturday':  calendar.SATURDAY,
            'Sunday':    calendar.SUNDAY
        }[day_name]
        return [week[day] for week in month_cal if week[day] != 0]

    def _ordinal(days):
        i = {
            '1st': 0, '2nd': 1, '3rd': 2,
            '4th': 3, '5th': 4, 'last': -1
        }[order]
        return days[i]

    def _teenth(days):
        return next(x for x in days if 12 < x < 20)

    if order == 'teenth':
        day = _teenth
    else:
        day = _ordinal

    return date(year, month, day(_week_days_in_month()))
