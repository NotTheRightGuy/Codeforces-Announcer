def convertSecondsToTime(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f"{hours} hours {minutes} minutes {seconds} seconds"
