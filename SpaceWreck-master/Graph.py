class Graph:
    # INIT FUNCTION
    def __init__(self, n, colors, rocket, lucky, edges):
        self.nodes = []
        self.rocket = rocket - 1
        self.lucky = lucky - 1
        nodes_edges = []
        # generate edges for each node
        for i in range(n):
            nodes_edges.append([])
        for edge in edges:
            nodes_edges[edge[0]].append(edge)
        # generate nodes
        for i in range(n):
            self.nodes.append(Node(i, colors[i], nodes_edges[i]))

    # SHOW ALL NODES DATA
    def show(self):
        for node in self.nodes:
            node.show()

    # CHECKS IF LUCKY OR ROCKET IS IN GOAL
    def goal_check(self):
        if self.nodes[self.rocket].color == 'goal' or self.nodes[self.lucky].color == 'goal':
            return True
        return False

    # RETURNS AVAILABLE ACTIONS
    def actions(self):
        actions = []
        # gets destination of where rocket and lucky can go using their location and node colors
        r_actions = self.nodes[self.rocket].destination(self.nodes[self.rocket].color, self.nodes[self.lucky].color)
        l_actions = self.nodes[self.lucky].destination(self.nodes[self.rocket].color, self.nodes[self.lucky].color)
        # makes action array with destination of node they can go and stores which one can do that action
        for action in r_actions:
            actions.append([action, 'r'])
        for action in l_actions:
            actions.append([action, 'l'])
        return actions

    # CHANGES ROCKY OR LUCKY LOCATION
    def do(self, action):
        # checks who is doing that action
        if action[1] == 'r':
            # changes his location
            self.rocket = action[0]
        else:
            self.lucky = action[0]


class Node:
    # INIT FUNCTION
    def __init__(self, number, color, edges):
        self.id = number
        self.color = color
        self.edges = edges

    # RETURNS A LIST OF NODES WHERE THAT NODE CAN GO
    def destination(self, corridor_color1, corridor_color2):
        dest = []
        # using edges of that node, checks nodes that it can go with given corridor colors
        for edge in self.edges:
            if edge[2] == corridor_color1 or edge[2] == corridor_color2:
                dest.append(edge[1])
        return dest

    # SHOWS NODE DATA
    def show(self):
        print("NODE NUMBER: ", self.id)
        print("WITH COLOR: ", self.color)
        print("AND EDGES: ", self.edges)
        print("=========================")
