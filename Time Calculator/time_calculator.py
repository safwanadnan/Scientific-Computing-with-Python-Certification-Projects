def add_time(start_time, duration, start_day=None):
    # Parse the start time
    start_hour, start_minute = [int(part) for part in start_time[:-3].split(':')]
    period = start_time[-2:]

    # Parse the duration
    duration_hour, duration_minute = [int(part) for part in duration.split(':')]

    # Convert start time to minutes
    start_minutes = start_hour * 60 + start_minute

    if period == 'PM':
        start_minutes += 12 * 60

    # Calculate the total minutes
    total_minutes = start_minutes + duration_hour * 60 + duration_minute

    # Calculate the new time
    new_minutes = total_minutes % (24 * 60)
    new_hour = new_minutes // 60
    new_minute = new_minutes % 60

    # Determine the period (AM or PM)
    period = 'AM' if new_hour < 12 else 'PM'
    new_hour = new_hour % 12 or 12

    # Format the new time
    new_time = f"{new_hour}:{new_minute:02d} {period}"

    # Calculate the number of days later
    days_later = total_minutes // (24 * 60)

    # Determine the day of the week (if provided)
    if start_day:
        start_day = start_day.lower()
        start_day_index = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'].index(start_day)
        new_day_index = (start_day_index + days_later) % 7
        new_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][new_day_index]
        new_time += f", {new_day}"

    # Determine the day count suffix
    if days_later == 1:
        day_count = "(next day)"
    elif days_later > 1:
        day_count = f"({days_later} days later)"
    else:
        day_count = ""

    # Append the day count to the new time
    new_time += f" {day_count}"

    return new_time.strip()
