# 0/1 Knapsack using Dynamic Programming
def knapsack(weights, values, capacity):
    n = len(weights)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            # If item can fit
            if weights[i - 1] <= w:

                # Include or exclude the item
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            else:
                # Item cannot fit
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity], dp


# -------- User Input --------

n = int(input("Enter number of items: "))

weights = []
values = []

for i in range(n):
    print("\nItem", i + 1)

    weight = int(input("Enter weight: "))
    value = int(input("Enter value: "))

    weights.append(weight)
    values.append(value)

capacity = int(input("\nEnter knapsack capacity: "))


# -------- Run Knapsack --------

max_value, dp = knapsack(weights, values, capacity)


# -------- Display Result --------

print("\nMaximum value:", max_value)

print("\nDP Table:")

for row in dp:
    print(row)