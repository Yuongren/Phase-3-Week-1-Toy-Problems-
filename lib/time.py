def convert_24_hour(hour, minute, period):
    #"""Convert 12-hour time to 24-hour time."""
    if period.lower() == "am":
        # For "am", if hour is 12, set it to 0; otherwise, keep it as is
        hour = 0 if hour == 12 else hour
    else:
        # For "pm", if hour is not 12, add 12 to it
        hour = hour + 12 if hour != 12 else 12

    # Format the result as a four-digit string (HHMM)
    return f"{hour:02d}{minute:02d}"

result_2 = convert_24_hour(8, 30, "pm")
print(result_2)