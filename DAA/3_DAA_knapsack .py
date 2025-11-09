def knapsaco():
    n = int(input("Enter number of items: "))
    weights = []
    values = []
    print("\nEnter weight and value (profit) for each item separated by space:")    
    for i in range(n):
        w,v = map(int,input(f"Enter the weight and values {i+1}").split())
        weights.append(w)
        values.append(v)

    Capacity = int(input("\nEnter maximum capacity of knapsack: "))
    dp = [0] * (Capacity+1)
    for i in range(n):
        w = weights[i]
        v = values[i]

        for cap in range(Capacity,w-1,-1):
            dp[cap] = max(dp[cap],v+dp[cap - w])
    print("\n Maximum profit that can be obtained:", dp[Capacity])

knapsaco()



/*
# Fractional Knapsack Problem using Greedy Method

def fractional_knapsack(value, weight, capacity):
    n = len(value)
    ratio = []

    # Calculate value/weight ratio for each item
    for i in range(n):
        ratio.append(value[i] / weight[i])

    # Combine all details into a list of tuples (ratio, value, weight)
    items = list(zip(ratio, value, weight))

    # Sort items by ratio in descending order
    items.sort(reverse=True)

    total_value = 0.0  # Total profit
    for r, v, w in items:
        if capacity >= w:
            capacity -= w
            total_value += v
        else:
            total_value += v * (capacity / w)
            break

    return total_value


# --- Taking input from user ---
n = int(input("Enter number of items: "))

value = []
weight = []

print("\nEnter value and weight for each item:")
for i in range(n):
    v = float(input(f"Value of item {i+1}: "))
    w = float(input(f"Weight of item {i+1}: "))
    value.append(v)
    weight.append(w)

capacity = float(input("\nEnter the capacity of the knapsack: "))

# Function call
max_value = fractional_knapsack(value, weight, capacity)
print("\nMaximum value in Knapsack =", max_value)

*/