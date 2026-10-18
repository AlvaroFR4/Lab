seconds = int(input("Seconds: "))
days = seconds // 86400
remainder = seconds % 86400

hours = remainder // 3600
remainder = remainder % 3600

minutes = remainder // 60
remaining_seconds = remainder % 60

print(f"{seconds} seconds are {days} days, {hours} hours, {minutes} minutes and {remaining_seconds} seconds")