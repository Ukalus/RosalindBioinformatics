# When finding the n-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation to generate terms for progressively larger values of n

# . This problem introduces us to the computational technique of dynamic programming, which successively builds up solutions by using the answers to smaller cases.

# Given: Positive integers n≤40
# and k≤5

# .

# Return: The total number of rabbit pairs that will be present after n
# months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).


## Rabbit Population: Pair of Rabbits


def rabbitPopulation(months,offspring, starting_pop):
    generation1, generation2 = starting_pop,starting_pop
    for i in range(months - 1):
        generation2, generation1 = generation1, generation1 + (generation2 * offspring)
    return(generation2) 


print(rabbitPopulation(5,3,1))