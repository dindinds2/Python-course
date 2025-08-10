from datetime import datetime
import random
def getRandomDate(startDate,endDate):
    print("random date and time between",startDate,"and",endDate)
    start_dt = datetime.strptime(startDate,"%dd/%mn/%yy")
    end_dt = datetime.strptime(endDate,"%dd/%mm/%yy")
    start_ts = start_dt.timestamp()
    end_ts = end_dt.timestamp()
    random_ts = random.uniform(start_ts,end_ts)
    return datetime.fromtimestamp(random_ts).strftime("%dd/%mm/%yy %H:%M:%S")
print("Random date",getRandomDate("01/01/1950","01/01/2050"))