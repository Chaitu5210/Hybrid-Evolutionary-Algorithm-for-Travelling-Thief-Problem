def Fitness(city:list, list:list, Knapsack_Weight:int , speed: int) -> int:
    weight, profit = 0, 0
    for i in range(len(list)):
        if list[i] == 1:
            weight = weight + float(city[i]['Weight'])
            profit = profit + int(city[i]['Profit'])
            pres_speed = speed *  (1 - (weight/Knapsack_Weight))
    print(profit,weight)
    if weight > Knapsack_Weight:
        return 0
    print("-----------------")
    return profit