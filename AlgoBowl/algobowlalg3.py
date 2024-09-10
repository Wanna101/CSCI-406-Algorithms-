import glob
import os
import networkx as nx

def minimize_testing_out(n, prerequisites):
    # Create a directed graph
    graph = nx.DiGraph()

    # Add edges representing prerequisites
    for i, prereqs in enumerate(prerequisites, start=1):
        for prereq in prereqs[1:]:
            graph.add_edge(prereq, i)

    tested_out_nodes = []

    # Remove nodes involved in cycles until the graph becomes a DAG
    while not nx.is_directed_acyclic_graph(graph):
        # Find cycles in the graph
        cycles = list(nx.find_cycle(graph))
        
        # if not cycles:
        #     # If no cycles remain, return the graph and the nodes tested out of
        
        # Count the number of times each node appears in cycles
        node_counts = {node: 0 for node in graph.nodes()}
        for cycle in cycles:
            for node in cycle:
                node_counts[node] += 1

        # Identify the node(s) with the maximum count
        max_count = max(node_counts.values())
        nodes_to_remove = {node for node, count in node_counts.items() if count == max_count}

        # Remove nodes involved in cycles and add them to the tested_out_nodes list
        rm_node = nodes_to_remove.pop()
        tested_out_nodes.append(rm_node)
        graph.remove_node(rm_node)

        # Debug print to show the order of nodes analyzed
        # print("Nodes analyzed:", sorted(node_counts.keys(), key=lambda x: node_counts[x], reverse=True))
    
    return tested_out_nodes, graph
    
def read_input(filename):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        prerequisites = [list(map(int, line.strip().split())) for line in f]
    #print("Read input:", n, prerequisites)
    return n, prerequisites

def process_file(filepath):
    n, prerequisites = read_input(filepath)
    tested_out_nodes, _ = minimize_testing_out (n, prerequisites)
    return tested_out_nodes

def main(input_dir, output_dir):
    # List all .txt files in input directory
    input_files = glob.glob(os.path.join(input_dir, '*.txt'))
    
    for input_filepath in input_files:
        tested_out_nodes = process_file(input_filepath)
        
        # Prepare output file path based on input file name
        base_filename = os.path.basename(input_filepath)
        output_filename = "output_" + base_filename  # Prefix with 'output_' or use another naming scheme
        output_filepath = os.path.join(output_dir, output_filename)
        
        # Write the output to a new file in the output directory
        with open(output_filepath, 'w') as f:
            f.write(f"{len(tested_out_nodes)}\n")
            f.write(' '.join(map(str, sorted(tested_out_nodes))))
        
        print(f"Processed {input_filepath} -> {output_filepath}")

# Now, when you call main, it expects two arguments
if __name__ == "__main__":
    input_dir = r'C:\Users\Owner\OneDrive - Colorado School of Mines\Documents\Mines\Spring 2024\algo\algoBowl\AlgoBowl-Team-Dumpling\all_inputs'
    output_dir = r'C:\Users\Owner\OneDrive - Colorado School of Mines\Documents\Mines\Spring 2024\algo\algoBowl\AlgoBowl-Team-Dumpling\all_outputs'
    main(input_dir, output_dir)

