from Retrieve_Parse_Data import Retrieve_Parse_Data
from Initialization import Parameter_Initialization
import random
from Fitness_Function import Fitness

# Initialize the dataset Path
file_path = "Hybrid-Evolutionary-Algorithm-for-Travelling-Thief-Problem/Dataset/TTP_50_Cities_Dataset.txt"


# initializing the genome
def Genome(length):
        return [random.randint(0,1) for _ in range(length)]

# initializing the population
def init_population(Population_Size: int, Genome_Length: int) -> list:
    return [Genome(Genome_Length) for _ in range(Population_Size)] 


Knapsack_Weight = 80
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
    print(Complete_Population)



    