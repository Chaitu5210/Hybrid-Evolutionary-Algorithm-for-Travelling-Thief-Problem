import random

def Parameter_Initialization(length):

    Population_size = int(0.60*length)
    Genome_Length = length 
    Generations=random.randint(1000,2000)

    '''It introduces enough random variation to maintain genetic diversity and
    prevent premature convergence without disrupting the search process too much.'''
    Mutation_Rate = 0.01

    '''It balances exploration of new solutions by combining individuals without 
    losing too much of the good traits.'''
    Crossover_Rate = 0.8

    return Population_size, Genome_Length, Generations, Mutation_Rate, Crossover_Rate