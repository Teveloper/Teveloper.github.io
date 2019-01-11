import time
import calendar

print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime())
print(time.strftime('%Y %B %d %A', time.localtime(time.time())))

print(calendar.calendar(2019))
print(calendar.prmonth(2019, 1))

print(calendar.weekday(2019, 1, 31))
