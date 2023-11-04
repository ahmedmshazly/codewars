def format_duration(seconds):
    if seconds == 0:
        return "now"

    years = seconds // (365 * 24 * 3600)
    days = (seconds % (365 * 24 * 3600)) // (24 * 3600)
    hours = (seconds % (24 * 3600)) // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    components = []

    if years > 0:
        components.append(f"{years} year{'s' if years > 1 else ''}")
    if days > 0:
        components.append(f"{days} day{'s' if days > 1 else ''}")
    if hours > 0:
        components.append(f"{hours} hour{'s' if hours > 1 else ''}")
    if minutes > 0:
        components.append(f"{minutes} minute{'s' if minutes > 1 else ''}")
    if seconds > 0:
        components.append(f"{seconds} second{'s' if seconds > 1 else ''}")

    if len(components) == 1:
        return components[0]
    elif len(components) == 2:
        return " and ".join(components)
    else:
        return ", ".join(components[:-1]) + " and " + components[-1]
