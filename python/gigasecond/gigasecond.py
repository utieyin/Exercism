from datetime import datetime, timedelta
from time import time
def add(moment):
    new_date=moment+timedelta(seconds=1000000000)
    return new_date
