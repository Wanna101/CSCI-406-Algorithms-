import networkx as nx

def find_min_classes_to_test_out_from_file(file_path):
    print("Reading input from file:", file_path)
    with open(file_path, 'r') as file:
        n = int(file.readline().strip())
        prerequisites = []
        for i in range(n):
            prereqs = list(map(int, file.readline().split()))
            prerequisites.append(prereqs)
            print("Read prerequisite for node", i+1, ":", prereqs)

    G = nx.DiGraph()
    for i in range(1, n + 1):
        G.add_node(i)

    for i, prereqs in enumerate(prerequisites):
        for prereq in prereqs[1:]:
            G.add_edge(prereq, i + 1)

    print("Constructed graph:")
    print(G.edges())

    classes_to_test_out = set()

    # Detect cycles in the graph
    while True:
        try:
            cycle_edges = nx.find_cycle(G, orientation='original')
        except nx.NetworkXNoCycle:
            break
        
        if cycle_edges:
            print("Found a cycle in the graph:")
            print("Cycle edges:", cycle_edges)
            # Extract nodes involved in the cycle
            for u, v, _ in cycle_edges:
                classes_to_test_out.add(v)
            # Remove edges involved in the cycle to break it
            for u, v, _ in cycle_edges:
                G.remove_edge(u, v)
        else:
            break

    if classes_to_test_out:
        print("The end graph has cycles and is not a Directed Acyclic Graph (DAG).")
    else:
        print("The end graph is a Directed Acyclic Graph (DAG).")

    print("Classes to test out:", classes_to_test_out)
    return len(classes_to_test_out), sorted(classes_to_test_out)

# Example usage with a file path
file_path = 'team_dumpling_input_1.txt'
num_classes, classes_to_test_out = find_min_classes_to_test_out_from_file(file_path)
print("Number of classes to test out:", num_classes)
print("Classes to test out:", *classes_to_test_out)
