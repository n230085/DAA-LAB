def prim(graph, start):
    visited = set()
    mst = []
    total_cost = 0

    # Start from the given vertex
    visited.add(start)

    while len(visited) < len(graph):

        minimum_edge = None
        minimum_weight = float('inf')

        # Find the minimum weight edge
        # connecting visited and unvisited vertices
        for u in visited:
            for v, weight in graph[u]:
                if v not in visited and weight < minimum_weight:
                    minimum_weight = weight
                    minimum_edge = (u, v, weight)

        # If no edge is found, graph is disconnected
        if minimum_edge is None:
            print("Graph is disconnected.")
            return

        u, v, weight = minimum_edge

        # Add edge to MST
        mst.append((u, v, weight))
        total_cost += weight

        # Mark new vertex as visited
        visited.add(v)

    # Display MST
    print("\nMinimum Spanning Tree:")

    for u, v, weight in mst:
        print(u, "--", v, ":", weight)

    print("Total cost:", total_cost)


# -------- User Input --------

# Number of vertices
n = int(input("Enter number of vertices: "))

# Enter vertices
vertices = input("Enter vertices separated by space: ").split()

if len(vertices) != n:
    print("Error: number of vertices does not match.")
    exit()

# Create graph
graph = {}

for vertex in vertices:
    graph[vertex] = []


# Number of edges
e = int(input("Enter number of edges: "))

# Enter edges
for i in range(e):
    print("\nEdge", i + 1)

    u = input("Enter source vertex: ")
    v = input("Enter destination vertex: ")
    w = int(input("Enter weight: "))

    if u not in graph or v not in graph:
        print("Error: vertex does not exist.")
        exit()

    # Undirected graph
    graph[u].append((v, w))
    graph[v].append((u, w))


# Starting vertex
start = input("\nEnter starting vertex: ")

if start not in graph:
    print("Error: starting vertex does not exist.")
    exit()

# Run Prim's Algorithm
prim(graph, start)