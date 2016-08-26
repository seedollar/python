from datetime import date, timedelta, datetime, time

halloween = date(2016, 10, 31)
print(halloween)
print(halloween.day)
print(halloween.month)
print(halloween.year)
print(halloween.isoformat())
print()


now = date.today()
print("Today: ", now)
two_days = timedelta(days=2)
day_after_tomorrow = now + two_days
print("Day after tomorrow: %s" % day_after_tomorrow)

one_week_from_today = now + 3.5*two_days
print("One week from Today: %s" % one_week_from_today)

yesterday = now - timedelta(days=1)
print("yesterday: ", yesterday)

print()

some_day = datetime(2016, 1,2,3,4,5,6)
print("Someday:", some_day)
print("some_day type:", type(some_day))
print("ISOFormat:", some_day.isoformat())

now = datetime.now()
print("Now: ", now)

launch_time = time(11,34,17)
launch_date = date.today() + timedelta(days=10)
launch_datetime = datetime.combine(launch_date, launch_time)
print("Launch datetime (combined): ", launch_datetime)


