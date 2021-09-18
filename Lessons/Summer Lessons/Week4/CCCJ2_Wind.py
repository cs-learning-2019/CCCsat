# Get the input
h = int(input())
M = int(input())

# Helper function
def A(h, t):
    return (-6 * (t ** 4)) + (h * (t ** 3)) + (2 * (t ** 2)) + (t)

# Main section
t = 1
hit_ground = False
while t < M:
    altitude = A(h, t)
    if altitude <= 0:
        print("The balloon first touches ground at hour:")
        print(t)
        hit_ground = True
        break
    t += 1

if hit_ground == False:
    print("The balloon does not touch ground in the given time.")


