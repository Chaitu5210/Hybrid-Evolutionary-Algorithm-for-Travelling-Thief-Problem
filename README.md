# Hybrid-Evolutionary-Algorithm-for-Travelling-Thief-Problem
This academic project focuses on developing a Hybrid Evolutionary Algorithm for the Travelling Thief Problem, which optimizes travel routes and item selection using genetic operators and local search to balance distance and profit constraints. Contributions are welcome, and we look forward to seeing your input!

Given a set of **points X**, where **X-1** represent cities with the following attributes:

- **Profit**
- **Weight**
- **X, Y Coordinates**

And one point representing the starting position of a thief, we need to calculate the maximum profit the thief can achieve under specific conditions.

## Conditions

1. The thief operates with a **knapsack** that has a defined capacity.
2. The **initial speed** of the thief is **100**.
3. As the weight of the knapsack increases, the speed decreases according to the formula:

   \[
   \text{Speed Reduction} = \left(\frac{\text{Current Knapsack Weight} + \text{Current Node Weight}}{\text{Knapsack Capacity}}\right) \times 100
   \]

## Goal

Determine the **maximum profit** achievable given the constraints of the knapsack capacity and the impact of weight on speed.

