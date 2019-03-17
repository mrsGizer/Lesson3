from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

dt_now = datetime.now()
delta_one_day = timedelta(days=1)
yesterday = dt_now - delta_one_day
delta_one_month = relativedelta(months=1)
last_month = dt_now - delta_one_month

print(yesterday.strftime('%d.%m.%Y'))
print(dt_now.strftime('%d.%m.%Y'))
print(last_month.strftime('%d.%m.%Y'))

user_date = '01/01/17 12:10:03.234567'
user_dt = datetime.strptime(user_date, '%d/%m/%y %H:%M:%S.%f')
print(user_dt)