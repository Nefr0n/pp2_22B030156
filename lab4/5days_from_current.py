from datetime import datetime, timedelta
    
ds = datetime.today() - timedelta(days = 5)
print(ds)

dy = datetime.today() - timedelta(days = 1)
dtd = datetime.today()
dtm = datetime.today() + timedelta(days = 1)
print(dy)
print(dtd)
print(dtm)