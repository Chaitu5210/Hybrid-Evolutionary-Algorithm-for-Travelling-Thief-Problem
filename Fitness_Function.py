def Fitness(cities: list, selection: list, knapsack_weight: int, speed: int) -> int:
    total_weight, total_profit = 0, 0
    
    for i in range(len(selection)):
        if selection[i] == 1:
            if i < len(cities):  # Ensure we don't go out of bounds
                total_weight += float(cities[i]['Weight'])
                total_profit += int(cities[i]['Profit'])
    
    # Calculate the effective speed based on the current weight
    pres_speed = speed * (1 - (total_weight / knapsack_weight))
    
    # Check if the total weight exceeds the knapsack capacity
    if total_weight > knapsack_weight:
        return 0
    
    return total_profit
