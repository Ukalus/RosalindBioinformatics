# Problem
# Figure 2. The Hamming distance between these two strings is 7. Mismatched symbols are colored red.

# Given two strings s
# and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t

# . See Figure 2.

# Given: Two DNA strings s
# and t

# of equal length (not exceeding 1 kbp).

# Return: The Hamming distance dH(s,t).

input1 = "GAGCCTACTAACGGGAT"
input2 = "CATCGTAATGACGGCCT"

def getHammingDistance(seq1, seq2):
    distance = 0
    for i in range(0,len(seq1)):
        if seq1[i] != seq2[i]:
            distance += 1
    return distance


print(getHammingDistance(input1,input2))