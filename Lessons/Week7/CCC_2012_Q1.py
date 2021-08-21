SpeedLimit = int(input("Enter the speed limit:"))
CarSpeed = int(input("Enter the recorded speed of the car:"))
SpeedOverBy = CarSpeed-SpeedLimit
if SpeedOverBy <= 0:
    print("Congratulations, you are within the speed limit!")
elif SpeedOverBy <= 20:
    print("You are speeding and your fine is $100.")
elif SpeedOverBy <= 30:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")
