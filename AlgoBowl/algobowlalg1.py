import os
import glob
import networkx as nx

def break_cycles(graph):
    #find one cycle at a time
    try:
        cycle = nx.find_cycle(graph, orientation='original')
        #return list of node sin the cycle if its found
        return[node for node, _, _ in cycle]
    except nx.NetworkXNoCycle:
        #raise an exception if no cycle is found
        raise Exception("No cycle found in the graph.")

def minimize_testing_out(n, prerequisites):
    # Create a directed graph
    graph = nx.DiGraph()

    # Add edges representing prerequisites
    for i, prereqs in enumerate(prerequisites, start=1):
        for prereq in prereqs[1:]:
            graph.add_edge(prereq, i)

    # Find cycles in the graph
    #cycles = list(nx.simple_cycles(graph))
    
    nodes_to_remove = set() #keep track of removed nodes
    
    #break each cycle till none is left
    while True:
        try:
            cycle_nodes = break_cycles(graph)
            if not cycle_nodes:
                break #no more cycles
        
            #remove a node based on degree
            node_to_remove = max(cycle_nodes, key=lambda node: graph.degree(node))
            nodes_to_remove.add(node_to_remove)
            #remove the selected node from graph
            graph.remove_node(node_to_remove)
        except Exception as e:
            #no more cycles, breaks the loop
            break
    return nodes_to_remove

def read_input(filename):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        prerequisites = [list(map(int, line.strip().split())) for line in f]
    #print("Read input:", n, prerequisites)
    return n, prerequisites

def process_file(filepath):
    n, prerequisites = read_input(filepath)
    testing_out = minimize_testing_out (n, prerequisites)
    return testing_out

def main(input_dir, output_dir):
    # List all .txt files in input directory
    input_files = glob.glob(os.path.join(input_dir, '*.txt'))
    
    for input_filepath in input_files:
        testing_out = process_file(input_filepath)
        
        # Prepare output file path based on input file name
        base_filename = os.path.basename(input_filepath)
        output_filename = "output_" + base_filename  # Prefix with 'output_' or use another naming scheme
        output_filepath = os.path.join(output_dir, output_filename)
        
        # Write the output to a new file in the output directory
        with open(output_filepath, 'w') as f:
            f.write(f"{len(testing_out)}\n")
            f.write(' '.join(map(str, sorted(testing_out))))
        
        print(f"Processed {input_filepath} -> {output_filepath}")

# Now, when you call main, it expects two arguments
if __name__ == "__main__":
    input_dir = r'C:\Users\Owner\OneDrive - Colorado School of Mines\Documents\Mines\Spring 2024\algo\algoBowl\AlgoBowl-Team-Dumpling\all_inputs'
    output_dir = r'C:\Users\Owner\OneDrive - Colorado School of Mines\Documents\Mines\Spring 2024\algo\algoBowl\AlgoBowl-Team-Dumpling\all_outputs'
    main(input_dir, output_dir)