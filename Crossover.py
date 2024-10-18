import random
def Crossover(parent1,parent2, Mutation_Rate):
    if random.random() < Mutation_Rate:
        Crossover_Point = random.randint(1,len(parent1)-1)
        return parent1[:Crossover_Point] + parent2[:Crossover_Point:], parent2[:Crossover_Point]+parent1[Crossover_Point:]
    else:
        return parent1, parent2