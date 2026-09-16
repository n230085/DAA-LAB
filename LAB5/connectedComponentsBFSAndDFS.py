from collections import deque

# ---------------- DFS ----------------
def dfs(graph, vertex, visited, component):
    visited.add(vertex)
    component.append(vertex)

    for neighbour in graph[vertex]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited, component)

# ---------------- BFS ----------------
def bfs(graph, start, visited, component):
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        component.append(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# -------- User Input --------

# Number of vertices
n = int(input("Enter number of vertices: "))

# Enter vertices
vertices = input("Enter the vertices separated by space: ").split()

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

    if u not in graph or v not in graph:
        print("Error: vertex does not exist.")
        exit()

    # Undirected graph
    graph[u].append(v)
    graph[v].append(u)


# -------- Choose BFS or DFS --------

print("\nChoose the technique:")
print("1. DFS (Depth-First Search)")
print("2. BFS (Breadth-First Search)")

choice = input("Enter your choice (1 or 2): ")


if choice not in ["1", "2"]:
    print("Invalid choice.")
    exit()


# -------- Find Connected Components --------

visited = set()
components = []

for vertex in vertices:

    if vertex not in visited:

        component = []

        if choice == "1":
            # Use DFS
            dfs(graph, vertex, visited, component)

        else:
            # Use BFS
            bfs(graph, vertex, visited, component)

        components.append(component)


# -------- Display Result --------

if choice == "1":
    print("\nUsing DFS")
else:
    print("\nUsing BFS")

print("Connected Components:")

for i, component in enumerate(components, 1):
    print("Component", i, ":", component)

print("\nTotal number of connected components:", len(components))