def add_time(start, duration, day=None):
    start = start.lower().split(":")
    duration = duration.split(":")

    if day:
        day = day.strip().lower().capitalize()

    week_days = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ]

    for i, item in enumerate(start):
        if "pm" in item or "am" in item:
            item = item.split(" ")

            # Convert the item to an integer, because we know it has to be one.
            start.append(int(item[0]))

            start.append(item[1])
            del start[i]

            # Break, because we know we reached the end of the list.
            break

        else:
            start[i] = int(item)

    # Turn the duration items into integers.
    for i, item in enumerate(duration):
        duration[i] = int(item)

    # Add the hours.
    hours = start[0] + duration[0]

    # Calculate the added minutes.
    minutes = start[1] + duration[1]

    # Determine period, "am", "pm".
    period = start[-1]

    # Calculate the additional hours that need to be added based off of how many minutes are given.
    add_hours = minutes / 60

    # Add the extra hours to the base hours.
    hours += add_hours
    hours = int(hours)

    # Calculate the leftover minutes.
    minutes = minutes % 60

    # Calculate the days passed.
    days = 0
    changes = 0

    # When the time switches to am is when the next day starts.
    # Get the number of time switches and see how many times the period changes to am.
    for i in range(int(hours / 12)):
        if period == "pm":
            period = "am"
            days += 1

        elif period == "am":
            period = "pm"

        changes += 1

    # Calculate if there needs to be a time change. "11:59 PM, 12:00 AM"
    if hours >= 12:
        if hours >= 13:
            hours = hours - (changes * 12)

    # If the minutes is only one digit, add a zero to the beggining of it.
    if len(str(minutes)) == 1:
        minutes = f"0{minutes}"

    if day:
        index = (days % len(week_days)) + (week_days.index(day))

        while index >= len(week_days):
            index = index - len(week_days)

        day = week_days[index]

    new_time = ""

    if hours == 0:
        hours = 12

    if day:
        if days > 1:
            new_time = f"{hours}:{minutes} {period.upper()}, {day} ({days} days later)"

        elif days == 1:
            new_time = f"{hours}:{minutes} {period.upper()}, {day} (next day)"

        else:
            new_time = f"{hours}:{minutes} {period.upper()}, {day}"

    else:
        if days == 1:
            new_time = f"{hours}:{minutes} {period.upper()} (next day)"

        elif days > 1:
            new_time = f"{hours}:{minutes} {period.upper()} ({days} days later)"

        else:
            new_time = f"{hours}:{minutes} {period.upper()}"

    return new_time
