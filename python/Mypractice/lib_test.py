from datetime import datetime


now = datetime.now()
print(now)
print(dir(datetime))
print(type(now))
print(repr("hello"))
dt = datetime(2015,4,19,12,20)
print(dt.timestamp())
t=1429417200.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))


cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
print(cday.timestamp())
print(cday.fromtimestamp(cday.timestamp()).timestamp())
print(cday.utcfromtimestamp(cday.timestamp()))

from datetime import timedelta,timezone
tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
print(now)
dt=now.replace(tzinfo=tz_utc_8)
print(dt)
print(now.timestamp())
print(dt.timestamp())

import re
b = re.match(r'UTC([\+\-]\d+):00$','UTC-7:00')
d = b.group(1)
print(int(d))
    
