import datetime as dt

a = dt.datetime(2004,11,24,3,11,59)
b = dt.datetime(2023,2,23,00,27,59)

print((b-a).total_seconds())