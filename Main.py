from Retrieve_Parse_Data import Retrieve_Parse_Data
from Initialization import Parameter_Initialization
import random
from Fitness_Function import Fitness
from Parent_Selection import parent_selection
from Crossover import Crossover
from Mutation import Mutate

# Initialize the dataset Path
file_path = "Hybrid-Evolutionary-Algorithm-for-Travelling-Thief-Problem/Dataset/TTP_50_Cities_Dataset.txt"

Knapsack_Weight = 290
Speed = 100



# initializing the genome
def Genome(length):
        return [random.randint(0,1) for _ in range(length)]

# initializing the population
def init_population(Population_Size: int, Genome_Length: int) -> list:
    return [Genome(Genome_Length) for _ in range(Population_Size)] 


Knapsack_Weight = 110
speed = 100

if __name__=="__main__":

    # Retrieve the cities Information from the dataset
    Cities_Data = Retrieve_Parse_Data(file_path)

    # Taking the total number of cities
    length = len(Cities_Data)
    
    # initializing the parameters
    Population_Size, Genome_Length, Generations, Mutation_Rate, Crossover_Rate = Parameter_Initialization(length)

    print(f'Initial Parameters:')
    print(f'Population_Size - {Population_Size}')
    print(f'Genome_Length - {Genome_Length}')
    print(f'Generations - {Generations}')
    print(f'Mutation_Rate - {Mutation_Rate}')
    print(f'Crossover_Rate - {Crossover_Rate}')


    # taking the population
    Complete_Population = init_population(Population_Size, Genome_Length)


    for generation in range(100):
         
        Fitness_Values=[Fitness(Cities_Data, individual , Knapsack_Weight, speed) for individual in Complete_Population]
        New_Population=[]

        for _ in range(Population_Size // 2):
            parent_1 = parent_selection(Complete_Population, Fitness_Values)
            parent_2 = parent_selection(Complete_Population, Fitness_Values)
            offspring_1,offspring_2 = Crossover(parent_1, parent_2, Mutation_Rate)
            New_Population.extend([Mutate(offspring_1, Mutation_Rate), Mutate(offspring_2, Mutation_Rate)])
        
        Complete_Population = New_Population
        Fitness_Values=[Fitness(Cities_Data, individual , Knapsack_Weight, speed) for individual in Complete_Population]
        best_fitness = max(Fitness_Values)
        print(f"Generation {generation}: Best Fitness = {best_fitness}")
    
    best_index=Fitness_Values.index(max(Fitness_Values))
    best_solution=Complete_Population[best_index]
    print(f"Best Solution: {best_solution}")
    print(f"Best Fitness: {Fitness(Cities_Data, best_solution, Knapsack_Weight, speed)}")



# Crossover_Rate
# Mutation_Rate


    