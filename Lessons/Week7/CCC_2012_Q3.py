# CCC 2012 J3 Icon Scaling
# Kavan Lam

# First get the input (the scale factor)
k = int(input())

# Create a list to represent the base icon
icon = ["*x*", " xx", "* *"]

# Now we scale the icon
# To do this we scale each line and for each line we duplicate it k times
for line in icon:
    scaled_line = "".join([k * character for character in line])
    for i in range(k):
        print(scaled_line)
