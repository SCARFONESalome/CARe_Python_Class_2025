#YOUR CODE FOR EX_0 INTERMEDIATE HERE
import math

initial_count = float(input("Enter the initial count:"))
final_count = float(input("Enter the final count:"))
time = float(input("Enter the time of growth :"))

growth_rate = (math.log(final_count) - math.log(initial_count))/time

print("The growth rate of the microbial culture is:", growth_rate)