#Write a program to display the current date and time in the format: "YYYY-MM-DD HH:MM:SS

from datetime import datetime 

now = datetime.now()

formatted_day_time = now.strftime("%y-%m-%d %H:%M:%S")

print(f"Current date and time : {formatted_day_time}")


'''
%Y: Year with century (e.g., 2023).
%y: Year without century (e.g., 23).
%m: Month as a zero-padded number (e.g., 01 to 12).
%d: Day of the month as a zero-padded number (e.g., 01 to 31).
%H: Hour (24-hour clock) as a zero-padded number (e.g., 00 to 23).
%I: Hour (12-hour clock) as a zero-padded number (e.g., 01 to 12).
%M: Minute as a zero-padded number (e.g., 00 to 59).
%S: Second as a zero-padded number (e.g., 00 to 59).
%p: AM or PM.
%A: Full weekday name (e.g., Monday).
%B: Full month name (e.g., January).
'''