from typing import Optional


# parameter renamed from time to time_seconds
# to avoid collision with standard library
def seconds_to_time(time_seconds: int) -> Optional[str]:
    """Convert a length of time in seconds to a string like hh:mm:ss or mm:ss.
    
    Uses hh:mm:ss only if time_seconds is at least an hour (at least 3600).
    """
    max_seconds = 359999
    if time_seconds > max_seconds:
        return

    time_minutes, time_seconds = divmod(time_seconds, 60)
    time_hours, time_minutes = divmod(time_minutes, 60)

    time_formatted = f'{time_minutes:02d}:{time_seconds:02d}'
    if time_hours:
        time_formatted = f'{time_hours:02d}:' + time_formatted
    return time_formatted


if __name__ == '__main__':
    print(seconds_to_time(3625))
    print(seconds_to_time(85))
    print(seconds_to_time(16))

    print(seconds_to_time(0))
    print(seconds_to_time(1))
    print(seconds_to_time(359999))
    print(seconds_to_time(360000))
