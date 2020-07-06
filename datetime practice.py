# from datetime import timezone,timedelta
# t_s = timezone(offset=timedelta(hours=5.5))
# print(t_s)

import datetime
import pytz

# a timestamp I'd like to convert
my_timestamp = datetime.datetime.now()

# create both timezone objects
old_timezone = pytz.timezone("US/Eastern")
new_timezone = pytz.timezone("Asia/Calcutta")
print(new_timezone)
a = str(datetime.datetime.now(new_timezone))
b = a.split('+')
print(b[0])
print(type(b[0]))