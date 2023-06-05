Bandwidth=int(input("Enter a the bandwidth in Mhz:- "))
mimo=int(input("Enter a value of mimo :- "))
CqiIndex = input("enter the cqi index (1-15): ")

SpecEffCqi = [0,0.1523,0.2344,0.3770,0.6016,0.8770,1.1758,1.4766,1.9141,2.4063,2.7305,3.3223,3.9023,4.5234,5.1152,5.5547]
y = SpecEffCqi[int(CqiIndex)]

Num_of_bits_in_one_PRB = 12 * 7 * y * 2   # Subcarriers * symbols * bits
RB = Bandwidth * 5
Num_of_bits_in_whole_Bandwidth = RB * Num_of_bits_in_one_PRB * mimo
Max_Tput = Num_of_bits_in_whole_Bandwidth / 1000
print("Maximum Throughput for given configuration : ",Max_Tput,"Mbps")

Practical_Tput = Max_Tput - (Max_Tput * 0.25)
print("Maximum Practical Throughput for given configuration : ",Practical_Tput,"Mbps")