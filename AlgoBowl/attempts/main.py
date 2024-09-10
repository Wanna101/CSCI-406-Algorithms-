import networkx as nx
import matplotlib.pyplot as plt
import random

def read_in(file_name):
    file_in = open(file_name)
    n_nodes = int(file_in.readline())
    m_edges = 0
    p_dict = {}
    for n in range(1, n_nodes + 1):
        current_input = file_in.readline().split()
        m_edges += int(current_input[0])
        p_dict[n] = current_input[1:]

    return n_nodes, m_edges, p_dict

def make_graph(n_nodes, p_dict):
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

def draw_graph(G):
    nx.draw_networkx(G)
    plt.show()

def gen_graph(n_nodes, max_p, file_name):
    with open(file_name, 'w') as file_out:
        file_out.write(str(n_nodes) + '\n')
        for i in range(1, n_nodes + 1):
            # randomly choose number of parents for i node
            i_p = random.randint(1, max_p)
            count = 0
            # choose i_p number of random parent
            cur_p_list = random.sample([k for k in range(1, n_nodes + 1) if k != i], i_p)
            # convert list of int to list of str
            cur_p_list = list(map(str, cur_p_list))
            # insert parent count
            cur_p_list.insert(0, str(i_p))
            # convert list to string with spacer and write to file
            file_out.write(' '.join(cur_p_list) + '\n')

n, m, p = read_in("test_input.txt")
graph = make_graph(n, p)
print([cycle for cycle in nx.simple_cycles(graph)])
# print([edge for edge in nx.dfs_edges(graph)])
