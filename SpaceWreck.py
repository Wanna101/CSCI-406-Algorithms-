import sys
import networkx as nx
from queue import Queue

def input(file):
    with open(file, 'r') as f:
        number_of_rooms, number_of_corridors = map(int, f.readline().split())
        colors_of_rooms = f.readline().split()
        rocket_initial, lucky_initial = map(int, f.readline().split())
        corridors = [list(map(str, line.split())) for line in f.readlines()]

        sorted_corridors = sorted(corridors, key=lambda x: int(x[0]))
        
        adjacencies = [None] * number_of_rooms
        
        for line in sorted_corridors:
            room_index = int(line[0])
            rc = (int(line[1]), line[2])
            
            if adjacencies[room_index] is None:
                adjacencies[room_index] = []
            adjacencies[room_index].append(rc)
            
    # COMMENT THIS OUT LATER
    # print(adjacencies)
    return number_of_rooms, number_of_corridors, colors_of_rooms, rocket_initial, lucky_initial, adjacencies

def get_room_color(number, colors_of_rooms):
    return colors_of_rooms[number - 1] 

def check_child(key, value, adjacencies_full):
    if key in adjacencies_full:
        if value in adjacencies_full[key]:
            return True            
        return False

    
def main():
    if len(sys.argv) < 2:
        print("python script.py input.txt")
        sys.exit(1)
    file = sys.argv[1]
    number_of_rooms, number_of_corridors, colors_of_rooms, rocket_initial, lucky_initial, adjacencies = input(file)
    adjacencies_full = {}
    starting_state = (rocket_initial, lucky_initial)
    
    graph = nx.DiGraph()
    

    for i in range(1, number_of_rooms + 1):
        for j in range(1, number_of_rooms + 1):
            state = (i, j)
            if (state[1] == number_of_rooms) or (state[0] == number_of_rooms):
                if state not in adjacencies_full:
                    adjacencies_full[state] = set()
                adjacencies_full[state].add((-1, -1))
                continue
            #if (state[0] is not None) and (state[0] in adjacencies) and (adjacencies[state[0]] is not None):
            try:
                for k in adjacencies[state[0]]:
                    if k[1] == get_room_color(state[1], colors_of_rooms):
                        added_tuple = (k[0], state[1])
                        if state not in adjacencies_full:
                            adjacencies_full[state] = set()
                        adjacencies_full[state].add((added_tuple))
            except TypeError:
                pass
            #if (state[1] is not None) and (state[1] in adjacencies) and (adjacencies[state[1]] is not None):
            try:
                for k in adjacencies[state[1]]:
                    if k[1] == get_room_color(state[0], colors_of_rooms):
                        added_tuple = (state[0], k[0])
                        if state not in adjacencies_full:
                            adjacencies_full[state] = set()
                        adjacencies_full[state].add((added_tuple))
            except TypeError:
                pass
    
    # print(graph.nodes)

    goal_states = set()
    for values in adjacencies_full.values():
        for value in values:
            if (value[0] == number_of_rooms) or (value[1] == number_of_rooms):
                goal_states.add(value)
    del_set = set()
    for key in adjacencies_full.keys():
        if (key[0] == number_of_rooms) or (key[1] == number_of_rooms):
            if key in goal_states:
                continue
            del_set.add(key)

    for key in del_set:
        del adjacencies_full[key]        
    
    for key, value in adjacencies_full.items():
        for v in value:
            # print(f"{key}: {v}")
            graph.add_edge(key, v)
    # print(graph.edges)

    all_paths = []
    try:
        for p in nx.all_shortest_paths(graph, starting_state, (-1, -1)):
            output = ""
            rocket_pos, lucky_pos = p[0]
            for n in range(1, len(p)):
                if rocket_pos == p[n][0]:
                    # rocket does not move
                    output += f"L{p[n][1]}"
                elif lucky_pos == p[n][1]:
                    # lucky does not move
                    output += f"R{p[n][0]}"
                rocket_pos, lucky_pos = p[n]
            all_paths.append(output)
        print(min(all_paths), end="")        
    except nx.NetworkXNoPath:
        # return nx.NetworkXNoPath("No path between %s and %s." % (starting_state, (-1, -1)))
        print("NO PATH", end="") 
        
if __name__ == "__main__":
    main()