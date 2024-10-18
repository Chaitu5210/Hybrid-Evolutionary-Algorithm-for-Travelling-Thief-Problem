import random
def parent_selection(population, fitness_values):
    total_fitness=sum(fitness_values)
    pick = random.uniform(0,total_fitness)
    current=0
    for individual,fitness_values in zip(population, fitness_values):
        current += fitness_values
        if current> pick:
            return individual





