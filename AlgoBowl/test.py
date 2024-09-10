import networkx as nx

'''
# Create a directed graph
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (3, 1)])

# Find a cycle starting from node 1
try:
    cycle_edges = nx.find_cycle(G, source=3, orientation='original')
    print("Cycle found:", cycle_edges)
except nx.NetworkXNoCycle:
    print("No cycle found starting from node 1")
'''

# import networkx as nx

# import networkx as nx

def dfs_cycle(G, start, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    for neighbor in G.neighbors(start):
        if neighbor in path:
            cycle_start = path.index(neighbor)
            cycle = path[cycle_start:]
            return cycle
        if neighbor not in visited:
            cycle = dfs_cycle(G, neighbor, visited, path)
            if cycle:
                return cycle

    path.pop()
    return None

# Create the graph
G = nx.DiGraph()
G.add_edge(1, 2)
G.add_edge(2, 1)
G.add_edge(1, 3)
G.add_edge(3, 1)
G.add_edge(2, 3)
G.add_edge(3, 2)

# Find the cycle starting from node 3 using DFS
start_node = 3
cycle = dfs_cycle(G, start_node)

# Print the cycle and visited nodes
if cycle:
    print("Cycle found:", cycle)
    print("Visited nodes:", cycle)
else:
    print("No cycle found starting from node", start_node)
