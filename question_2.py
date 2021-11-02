import datetime
from typing import Optional


HOUR_SECONDS = 60 * 60


# parameter renamed from time to time_seconds
# to avoid collision with standard library
def seconds_to_time(time_seconds: int) -> Optional[str]:
    max_seconds = 359999
    if time_seconds > max_seconds:
        return

    if time_seconds > HOUR_SECONDS:
        time_format = '%H:%M:%S'
        # match desired output with behaivour of time module
        # time_seconds += 1
    else:
        time_format = '%M:%S'

    time_delta = datetime.timedelta(seconds=time_seconds)
    return time_delta.strftime(time_format)


if __name__ == '__main__':
    print(seconds_to_time(3624))
    print(seconds_to_time(85))
    print(seconds_to_time(16))

    print(seconds_to_time(0))
    print(seconds_to_time(1))
