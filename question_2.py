import time
from typing import Optional


def seconds_to_time(time_seconds: int) -> Optional[str]:
    max = 359999
    if time_seconds > max:
        return

    # match desired output with behaivour of time module
    time_seconds += 1

    time_tuple = time.gmtime(time_seconds)
    return time.strftime('%H:%M:%S', time_tuple)


if __name__ == '__main__':
    print(seconds_to_time(3624))
    print(seconds_to_time(85))
