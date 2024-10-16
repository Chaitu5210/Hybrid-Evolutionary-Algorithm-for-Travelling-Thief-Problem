from Retrieve_Parse_Data import Retrieve_Parse_Data
from Initialization import Parameter_Initialization


# Initialize the dataset Path
file_path="Hybrid-Evolutionary-Algorithm-for-Travelling-Thief-Problem/Dataset/TTP_50_Cities_Dataset.txt"

 




if __name__=="__main__":

    # Retrieve the cities Information from the dataset
    Cities_Data = Retrieve_Parse_Data(file_path)

    # Taking the total number of cities
    length=len(Cities_Data)
    
    # initializing the parameters
    Population_Size, Genome_Length, Generations, Mutation_Rate, Crossover_Rate = Parameter_Initialization(length)

    print(Population_Size, Genome_Length, Generations, Mutation_Rate, Crossover_Rate)
    