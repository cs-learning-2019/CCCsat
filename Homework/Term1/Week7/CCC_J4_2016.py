# Python CCC
# J4 2016 Arrival Time
# Kavan Lam
# Nov 6, 2021

# First get the input
start_time = input().split(":")
hour = int(start_time[0])
minute = int(start_time[1])

# Define a helper function to print the answer given the hour and minute
def print_time(hour, minute):
    # Deal with the hour
    hour = hour % 24
    str_hour = str(hour)
    if len(str_hour) < 2:
        str_hour = "0" + str_hour

    # Deal with the minute
    str_minute = str(minute)
    if len(str_minute) < 2:
        str_minute = "0" + str_minute

    print(str_hour + ":" + str_minute)

# If the starting time is 7pm or greater then just add two hours and that is the answer
if hour > 19:
    finish_hour = hour + 2
    finish_minute = minute
    print_time(finish_hour, finish_minute)
# Otherwise we process the time minute by minute until the commute time is up
else:
    # Define the slow time regions
    slow_1_start = 7 * 60
    slow_1_end = 10 * 60

    slow_2_start = 15 * 60
    slow_2_end = 19 * 60

    current_minutes = (hour * 60) + minute
    total_time = 240 # 4 hours = 240 minutes is the worse case commute time

    # Process the commute minute by minute to get the finishing time
    while total_time > 0:
        if current_minutes < slow_1_end and current_minutes >= slow_1_start:
            total_time -= 1
        elif current_minutes < slow_2_end and current_minutes >= slow_2_start:
            total_time -= 1
        else:
            total_time -= 2

        current_minutes += 1

    # From the current_minutes we get the final time
    hour = current_minutes // 60 % 24
    minute = current_minutes % 60
    print_time(hour, minute)






    



    


