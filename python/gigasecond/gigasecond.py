from datetime import datetime, timedelta
from time import time
def add(moment):
    new_date=moment+timedelta(seconds=1000000000)
    print(new_date)
    return new_date


add(datetime(2011, 4, 25, 0, 0))