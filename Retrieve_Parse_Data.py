def Retrieve_Parse_Data(file_path: str) -> list:
    # Setup the dataset
    City_Data=[]

    # Taking Things into the Dictionary
    with open(file_path,'r') as file:
        file.readline()
        for line in file:
            information=line.split()

            City_Number = information[0]
            X_Coordinate = information[1]
            Y_coordinate = information[2]
            City_Name = information[3]
            Weight = information[4]
            Profit = information[5]


            # Appending parsed data to the list
            City_Data.append({
                    'City_Number' : City_Number,
                    'X_Coordinate' : X_Coordinate,
                    'Y_coordinate' : Y_coordinate,
                    'City_Name' : City_Name,
                    'Weight' : Weight,
                    'Profit' : Profit
                })
        
    return City_Data


        