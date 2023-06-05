Bandwidth=int(input("Enter a the bandwidth in Mhz:- "))
mimo=int(input("Enter a value of mimo :- "))
mcs=int(input("Enter Modulation scheme (in bits,e.g enter 6 for 64Qam):- "))


Num_of_bits_in_one_PRB = 12 * 7 * mcs * 2   # Subcarriers * symbols * bits
RB = Bandwidth * 5
Num_of_bits_in_whole_Bandwidth = RB * Num_of_bits_in_one_PRB * mimo
Max_Tput = Num_of_bits_in_whole_Bandwidth / 1000
print("Maximum Throughput for given configuration : ",Max_Tput,"Mbps")

Practical_Tput = Max_Tput - (Max_Tput * 0.25)
print("Maximum Practical Throughput for given configuration : ",Practical_Tput,"Mbps")









