def dijkstra(graph, source):
    # Initialize distances
    dist = {}

    for vertex in graph:
        dist[vertex] = float('inf')

    # Distance from source to itself is 0
    dist[source] = 0

    # Set of visited vertices
    S = set()

    while len(S) < len(graph):

        # Find the unvisited vertex with minimum distance
        u = None

        for vertex in graph:
            if vertex not in S:
                if u is None or dist[vertex] < dist[u]:
                    u = vertex

        # If no reachable unvisited vertex remains, stop
        if u is None or dist[u] == float('inf'):
            break

        # Mark u as visited
        S.add(u)

        # Relax all neighbouring vertices
        for v, weight in graph[u]:
            new_distance = dist[u] + weight

            if new_distance < dist[v]:
                dist[v] = new_distance

    return dist


# -------- User Input --------

# Number of vertices
n = int(input("Enter number of vertices: "))

# Enter vertices
vertices = input("Enter the vertices separated by space: ").split()

if len(vertices) != n:
    print("Error: number of vertices does not match.")
    exit()

# Create empty graph
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

    # Check whether vertices exist
    if u not in graph or v not in graph:
        print("Error: vertex does not exist.")
        exit()

    # Dijkstra cannot handle negative weights
    if w < 0:
        print("Error: Dijkstra's algorithm does not allow negative weights.")
        exit()

    # For an undirected graph
    graph[u].append((v, w))
    graph[v].append((u, w))


# Source vertex
source = input("\nEnter source vertex: ")

if source not in graph:
    print("Error: source vertex does not exist.")
    exit()


# Run Dijkstra's algorithm
distances = dijkstra(graph, source)

# Display shortest distances
print("\nShortest distances from", source)

for vertex in vertices:
    if distances[vertex] == float('inf'):
        print(vertex, ": Not reachable")
    else:
        print(vertex, ":", distances[vertex])