# Kavan Lam
# CCC 2011 J1 Which Alien
# July 24, 2021

# Get the input
print("How many antennas?")
antennas = int(input())

print("How many eyes?")
eyes = int(input())

# Get the answer
# Check to see if it is a TroyMartian
if antennas >= 3 and eyes <= 4:
    print("TroyMartian")

# Check to see if it is a VladSaturnian
if antennas <= 6 and eyes >= 2:
    print("VladSaturnian")

# Check to see if it is a GraemeMercurian
if antennas <= 2 and eyes <= 3:
    print("GraemeMercurian")
