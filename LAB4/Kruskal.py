def kruskal(vertices, edges):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    parent = {v: v for v in vertices}

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(a, b):
        rootA = find(a)
        rootB = find(b)

        if rootA != rootB:
            parent[rootB] = rootA
            return True

        return False

    mst = []
    total_cost = 0

    for u, v, weight in edges:
        # Add edge only if it doesn't form a cycle
        if union(u, v):
            mst.append((u, v, weight))
            total_cost += weight
        # MST contains V-1 edges
        if len(mst) == len(vertices) - 1:
            break

    return mst, total_cost

# Vertices
vertices = ['A', 'B', 'C', 'D','E','F']
# Edges: (node1,node2 weight)
edges = [
    ('A', 'B', 7),
    ('A', 'C', 2),
    ('A', 'D', 6),
    ('B', 'C', 6),
    ('B', 'E', 4),
    ('C','D',6),
    ('C','F',5),
    ('C','E',9),
    ('D','F',3),
    ('E','F',8)
]

mst, cost = kruskal(vertices, edges)
print("Edges in MST:")
for edge in mst:
    print(edge)

print("Minimum Cost:", cost)