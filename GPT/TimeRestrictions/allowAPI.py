from datetime import datetime
import pytz

# Check and return false if current Oslo time is in the range
fromTime = (6, 50)  # 14:00
toTime = (7, 20)  # 14:30

def checkTimeInRange(time, start, end):
    """Check if 'time' is within the range specified by 'start' and 'end'."""
    return start <= time <= end

def legalToUseAPI():
    tz_Oslo = pytz.timezone('Europe/Oslo') 
    datetime_Oslo = datetime.now(tz_Oslo)

    # Create start and end times using the defined interval
    start_time = datetime_Oslo.replace(hour=fromTime[0], minute=fromTime[1], second=0, microsecond=0)
    end_time = datetime_Oslo.replace(hour=toTime[0], minute=toTime[1], second=0, microsecond=0)

    return not checkTimeInRange(datetime_Oslo, start_time, end_time) 

print(legalToUseAPI())