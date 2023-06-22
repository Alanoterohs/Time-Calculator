from time_calculator import time_calculator

print(time_calculator("3:00 PM", "3:10", weekDay=""))
print(time_calculator("11:30 AM", "2:32", weekDay="Monday"))
print(time_calculator("11:43 AM", "00:20", weekDay=""))
print(time_calculator("10:10 PM", "3:30", weekDay=""))
print(time_calculator("11:43 PM", "24:20", weekDay="tueSday"))
print(time_calculator("6:30 PM", "205:12", weekDay=""))


# Returns: 6:10 PM
# Returns: 2:02 PM, Monday
# Returns: 12:03 PM
# Returns: 1:40 AM (next day)
# Returns: 12:03 AM, Thursday (2 days later)
# Returns: 7:42 AM (9 days later)
