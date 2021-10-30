# CCC 2017 J4 Favourite Times 
# Kavan Lam
# Oct 23, 2021

# Get inputs
D = int(input())

# Define a helper function to determine if a given time forms an arithmetic sequence
def is_arithmetic_sequence(hour, minute):
    digits = []

    # Add the numbers in hour to the digits list
    for digit in str(hour):
        digits.append(int(digit))

    # Add the numbers in minute to the digits list
    # Note if minutes is less than 10 then we need to add an extra zero
    if minute < 10:
        digits.append(0)
        
    for digit in str(minute):
        digits.append(int(digit))

    # Now ensure that the differences are constant
    difference = None
    for i in range(0, len(digits) - 1):
        diff = digits[i + 1] - digits[i]
        if difference == None:
            difference = diff
        else:
            if difference != diff:
                return False

    return True

# Go through the all the times minute by minute and count the number of arithmetic sequences
# Note that a day contains 1440 minutes. So lets find the number of arithmetic sequences
# within a day then mulitply that by the number of days and then manually count the rest
# Also note that since we have a 12-hour clock this means we only need to do half the day
# so 720 minutes

# Create variables to hold onto current time and number of arithmetic sequences found
hour = 12
minute = 0
arithmetic_seqs_found = 0


if D <= 720:
    for i in range(D):
        minute += 1
        
        if minute == 60:
            minute = 0
            hour += 1

            if hour == 13:
                hour = 1

        if is_arithmetic_sequence(hour, minute) == True:
            arithmetic_seqs_found += 1

    print(arithmetic_seqs_found)
else:
    for i in range(720):
        minute += 1
        
        if minute == 60:
            minute = 0
            hour += 1

            if hour == 13:
                hour = 1

        if is_arithmetic_sequence(hour, minute) == True:
            arithmetic_seqs_found += 1

    arithmetic_seqs_found = arithmetic_seqs_found * (D // 720)
    hour = 12
    minute = 0

    for i in range(D % 720):
        minute += 1
        
        if minute == 60:
            minute = 0
            hour += 1

            if hour == 13:
                hour = 1

        if is_arithmetic_sequence(hour, minute) == True:
            arithmetic_seqs_found += 1

    print(arithmetic_seqs_found)
    

















