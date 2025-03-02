#Write a program to display the current date and time in the format: "YYYY-MM-DD HH:MM:SS

from datetime import datetime 

now = datetime.now()

formatted_day_time = now.strftime("%y-%m-%d %H:%M:%S")

print(f"Current date and time : {formatted_day_time}")