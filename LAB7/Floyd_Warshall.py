import math

def floyd_warshall(graph):
    """
    Computes all-pairs shortest paths using the Floyd-Warshall algorithm.
    Parameters:
    graph (list of list of float/int): Adjacency matrix where graph[i][j] represents
                                       the weight of the directed edge from i to j.
                                       Disconnected paths should be set to math.inf,
                                       and self-loops graph[i][i] set to 0.
    Returns:
    dist (list of list of float/int): Matrix containing the shortest path distance between
                                      every pair of vertices (i, j).
    """
    V = len(graph)

    # Step 1: Initialize distance matrix D^0 identical to input weight matrix
    dist = [row[:] for row in graph]

    # Step 2: Three nested loops: intermediate (k), source (i), destination (j)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # Step 3: Relaxation using the recurrence relation
                # D[i][j] = min(D[i][j], D[i][k] + D[k][j])
                if dist[i][k] != math.inf and dist[k][j] != math.inf:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Detection of negative-weight cycles (Optional check based on negative diagonals)
    for i in range(V):
        if dist[i][i] < 0:
            print(f"Warning: Negative weight cycle detected passing through vertex {i}!")

    return dist

# --- Example Execution & Testing ---
if __name__ == "__main__":
    INF = math.inf

    # Example 5-vertex directed weighted graph
    example_graph = [
        [0, 3,8,INF,-4 ],
        [INF, 0,INF,1,7],
        [INF,4, 0,INF,INF],
        [2,INF, -5, 0,INF],
        [INF,INF,INF,6,0]
    ]

    shortest_paths = floyd_warshall(example_graph)

    print("All-Pairs Shortest Path Distance Matrix:")
    for row in shortest_paths:
        formatted_row = [f"{val:4}" if val != INF else " INF" for val in row]
        print(" ".join(formatted_row))