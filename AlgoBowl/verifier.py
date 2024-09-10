import networkx as nx

def make_our_graph(our_file_name):
    file_in = open(our_file_name)
    n_nodes = int(file_in.readline())
    m_edges = 0
    p_dict = {}
    for n in range(1, n_nodes + 1):
        current_input = file_in.readline().split()
        m_edges += int(current_input[0])
        p_dict[n] = current_input[1:]

    # make graph
    G = nx.DiGraph()
    # add nodes
    for n in range(1, n_nodes+1):
        G.add_node(n)
    # add edges
    for c_node, p_nodes in p_dict.items():
        for p in p_nodes:
            G.add_edge(int(p), c_node)

    return G

def read_in_result(their_file_name):
    file_in = open(their_file_name)
    n_delete = int(file_in.readline())
    node_to_remove = file_in.readline().split()
    
    return n_delete, node_to_remove

def check(our_graph, node_to_remove):
    for node in node_to_remove:
        our_graph.remove_node(int(node))

    return nx.is_directed_acyclic_graph(our_graph)

our_graph = make_our_graph('input_group725.txt')
_, their_removal = read_in_result('verification_outputs/outputs/output_from_770_to_725.txt')
print(check(our_graph, their_removal))
