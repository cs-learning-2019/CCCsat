# First get the input
a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

# Figure out how far each person got
def distance_moved(forward, backward, max_steps):
    displacement_per_cycle = forward - backward
    num_of_full_cycles = max_steps // (forward + backward)
    partial_cycle = max_steps % (forward + backward)
    
    distance_moved = num_of_full_cycles * displacement_per_cycle
    if partial_cycle > forward:
        distance_moved += forward - (partial_cycle - forward)
    else:
        distance_moved += partial_cycle

    return distance_moved

nikky = distance_moved(a, b, s)
bryon = distance_moved(c, d, s)

if nikky > bryon:
    print("Nikky")
elif nikky < bryon:
    print("Byron")
else:
    print("Tied")




