#YOUR CODE FOR EX_0 ADVANCED HERE

sequence = input("Enter your DNA sequence:")
is_A_T_C_G = ["A","T","C","G"]
if sequence  = print("Your DNA sequence is valid")
else: print("Your DNA sequence isn't valid")

print("The length of the sequence is:",(len(sequence) ))

count_A = sequence.count("A")
count_T = sequence.count("T")
count_G = sequence.count("G")
count_C = sequence.count("C")

print("Numbers of A is:", count_A)
print("Numbers of T is:", count_T)
print("Numbers of G is:", count_G)
print("Numbers of C is:", count_C)

count_GC = sequence.count("G") + sequence.count("C")
print("Content of GC is:", count_GC)