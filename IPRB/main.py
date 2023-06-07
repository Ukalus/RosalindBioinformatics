# Probability is the mathematical study of randomly occurring phenomena. We will model such a phenomenon with a random variable, which is simply a variable that can take a number of different distinct outcomes depending on the result of an underlying random process.

# For example, say that we have a bag containing 3 red balls and 2 blue balls. If we let X
# represent the random variable corresponding to the color of a drawn ball, then the probability of each of the two outcomes is given by Pr(X=red)=35 and Pr(X=blue)=25

# .

# Random variables can be combined to yield new random variables. Returning to the ball example, let Y
# model the color of a second ball drawn from the bag (without replacing the first ball). The probability of Y being red depends on whether the first ball was red or blue. To represent all outcomes of X and Y, we therefore use a probability tree diagram. This branching diagram represents all possible individual probabilities for X and Y

# , with outcomes at the endpoints ("leaves") of the tree. The probability of any outcome is given by the product of probabilities along the path from the beginning of the tree; see Figure 2 for an illustrative example.

# An event is simply a collection of outcomes. Because outcomes are distinct, the probability of an event can be written as the sum of the probabilities of its constituent outcomes. For our colored ball example, let A
# be the event "Y is blue." Pr(A) is equal to the sum of the probabilities of two different outcomes: Pr(X=blue and Y=blue)+Pr(X=red and Y=blue), or 310+110=25

# Given: Three positive integers k
# , m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n

# are homozygous recessive.

# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

# Note: THIS IS STILL NOT WORKING :(

from enum import Enum
class Allele(Enum):
    DOMINANT = 1,
    RECESSIVE = 2,
    HET = 3

def mate(x,y):
    if x == Allele.DOMINANT and y == Allele.DOMINANT:
        return [Allele.DOMINANT]*4
    if x == Allele.RECESSIVE and y == Allele.RECESSIVE:
        return [Allele.RECESSIVE]*4
    if x == Allele.HET and y == Allele.HET:
        return [Allele.DOMINANT,Allele.HET,Allele.HET,Allele.RECESSIVE]
    if x == Allele.HET:
        return [Allele.HET, Allele.HET, y, y]
    if y == Allele.HET:
        return [Allele.HET, Allele.HET, x, x] 
    else:
        return [Allele.HET]*4

def getPairs(organisms):
    
    if len(organisms) < 2:
        return list()
    first = organisms[0]
    pairs = [(first,organisms[second_index]) for second_index in range(1,len(organisms))]
    other_pairs = getPairs(organisms[1:])
    pairs.extend(other_pairs)
    return pairs
          
def f(k,m,n):
    organisms = list()
    for i in range(k):
        organisms.append(Allele.DOMINANT)
    for i in range(m):
        organisms.append(Allele.RECESSIVE)
    for i in range(n):
        organisms.append(Allele.HET)
    pairs = getPairs(organisms)
    children_list = [mate(*p) for p in pairs]
    children = [child for sublist in children_list for child in sublist]
    count_children = len(children)
    count_dominant_presence = 0
    for child in children:
        if child is not Allele.RECESSIVE:
            count_dominant_presence += 1
    return round(count_dominant_presence / count_children,5)


k = 21
m = 21
n = 30

print(f(k,m,n))
