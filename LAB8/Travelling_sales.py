def tsp_held_karp(C):

    n = len(C)

    # All cities except starting city 0
    all_other_cities = frozenset(range(1, n))

    # Memoization dictionary
    memo = {}

    def g(i, S):
        # Base case:
        # If no cities are left, return cost from city i to city 0
        if not S:
            return C[i][0]

        # If already calculated, return stored value
        if (i, S) in memo:
            return memo[(i, S)]

        min_cost = float('inf')

        # Try every city j in S
        for j in S:

            # Remove j from the remaining set
            remaining_set = S - {j}

            # Cost = i -> j + minimum cost from j
            # through the remaining cities
            cost = C[i][j] + g(j, remaining_set)

            # Update minimum cost
            if cost < min_cost:
                min_cost = cost

        # Store result in memo
        memo[(i, S)] = min_cost

        return min_cost

    # Start from city 0
    return g(0, all_other_cities)


# -----------------------------
# Example
# -----------------------------

C = [
    [0, 7, 0, 1, 1],
    [7, 0, 3, 0, 8],
    [0, 3, 0, 6, 2],
    [1, 0, 6, 0, 7],
    [1, 8, 2, 7, 0]
]

minimum_cost = tsp_held_karp(C)

print("Minimum cost:", minimum_cost)