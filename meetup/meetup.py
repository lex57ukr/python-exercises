import calendar
from datetime import date
from functools import partial


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

    def _ordinal(i, days):
        return days[i]

    def _teenth(days):
        return next(x for x in days if 12 < x < 20)

    day = {
        '1st':    partial(_ordinal, 0),
        '2nd':    partial(_ordinal, 1),
        '3rd':    partial(_ordinal, 2),
        '4th':    partial(_ordinal, 3),
        '5th':    partial(_ordinal, 4),
        'last':   partial(_ordinal, -1),
        'teenth': _teenth
    }[order](_week_days_in_month())

    return date(year, month, day)
