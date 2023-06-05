import math

input1 = input("Enter the 5G channel Bandwidth (MHz): ")
input2 = input("Enter the subcarrier spacing (KHz): ")
mimolayers = input("Enter the mimo layers (1 to 4): ")

x = int(input1) * 1000 / int(input2) / 12
NumPRBs = x - 4
NumPRBs = math.floor(NumPRBs)
print("Available number of PRBs is : " + str(NumPRBs))
Dlslots = 1600

Throughput = 977 * int(NumPRBs) * int(Dlslots) * int(mimolayers) / 1000 / 1000
print("Maximum Throughput for given configuration is : " + str(Throughput))
