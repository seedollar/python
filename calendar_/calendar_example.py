import calendar

print(calendar.isleap(2010))

for year in range(2000, 3000, 4):
    print("Year {1}: {0}".format(calendar.isleap(year), year))

