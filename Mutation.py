import random

def Mutate(genome, mutation_rate):
    for point in genome:
        if random.random() < mutation_rate:
            point = abs(point - 1)  # Flip binary value
    return genome
