import networkx as nx

def minimize_testing_out(n, prerequisites):
    # Create a directed graph
    graph = nx.DiGraph()

    # Add edges representing prerequisites
    for i, prereqs in enumerate(prerequisites, start=1):
        for prereq in prereqs[1:]:
            graph.add_edge(prereq, i)

    # Find cycles in the graph
    cycles = list(nx.simple_cycles(graph))

    if cycles:
        # Count the number of times each node appears in cycles
        node_counts = {node: 0 for node in graph.nodes()}
        for cycle in cycles:
            for node in cycle:
                node_counts[node] += 1

        # Identify the node(s) with the maximum count
        max_count = max(node_counts.values())
        nodes_to_remove = {node for node, count in node_counts.items() if count == max_count}

        # Debug print to show the order of nodes analyzed
        print("Nodes analyzed:", sorted(node_counts.keys(), key=lambda x: node_counts[x], reverse=True))

        return nodes_to_remove, graph
    else:
        return set(), graph

def read_input(filename):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        prerequisites = [list(map(int, line.strip().split())) for line in f]
    print("Read input:", n, prerequisites)
    return n, prerequisites

def main():
    filename = 'team_dumpling_input_2.txt'  
    n, prerequisites = read_input(filename)
    testing_out, G = minimize_testing_out(n, prerequisites)

    # Output
    print(len(testing_out))
    print(*testing_out)

    # verify
    for node in testing_out:
        G.remove_node(node)

    print(f"is a DAG: {nx.is_directed_acyclic_graph(G)}")

if __name__ == "__main__":
    main()
