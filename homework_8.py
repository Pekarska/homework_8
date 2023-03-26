from datetime import datetime, timedelta
from collections import defaultdict
users = [{'name': 'Anna', 'birthday': datetime(1997, 3, 25)}, {'name': 'Dima', 'birthday': datetime(1997, 5, 8)},
         {'name': 'Natali', 'birthday': datetime(1969, 3, 27)}, {'name': 'Margo', 'birthday': datetime(1997, 5, 4)}]
def get_birthdays_per_week(users):
    r = defaultdict(list)
    current_date = datetime.now().date()
    cur_week_day = current_date.weekday() + 1

    future_datetime = current_date + timedelta(days=7 - cur_week_day + 1)
    future_datetime_next_seven = future_datetime + timedelta(days=4)


    for i in users:
        b = i['birthday']
        b_month = int(datetime.strftime(b, '%-m'))
        b_day = int(datetime.strftime(b, '%-d'))
        n = datetime(current_date.year, b_month, b_day).date()
        if future_datetime <= n <= future_datetime_next_seven:
            month_day = datetime.strftime(b, '%')
            week_day = datetime.strftime(b, '%A')
            if week_day == 'Saturday' or week_day == 'Sunday':
                week_day = 'Monday'
            r[week_day].append(i['name'])

    for key, value in r.items():
        return (f"{key}: {','.join(r[key])}")

result = get_birthdays_per_week(users)
print(result)



